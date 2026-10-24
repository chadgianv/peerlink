"""Local demo group workflow regression checks."""
import tempfile
import unittest
from pathlib import Path
from app import requests_store,group_store
from app.main import GroupJoinRequest,GroupJoinDecision,join_group,decide_group,group_inbox,demo_groups
from fastapi import HTTPException

class GroupTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.old=requests_store.DB_PATH
        requests_store.DB_PATH=Path(self.tmp.name)/"demo.sqlite3"
    def tearDown(self):
        requests_store.DB_PATH=self.old
        self.tmp.cleanup()

    def test_pending_approval_updates_membership(self):
        pending=join_group(GroupJoinRequest(account_id="alex",group_id="g1"))
        self.assertEqual(pending["status"],"pending")
        self.assertEqual(group_inbox("joshua")["requests"][0]["id"],pending["id"])
        approved=decide_group(pending["id"],GroupJoinDecision(account_id="joshua",status="accepted"))
        self.assertEqual(approved["status"],"accepted")
        self.assertEqual(group_inbox("alex")["requests"][0]["status"],"accepted")
        group=next(g for g in demo_groups()["groups"] if g["id"]=="g1")
        self.assertEqual(group["members"],4)
        self.assertEqual(group["available_seats"],1)

    def test_duplicate_full_and_unauthorized(self):
        pending=join_group(GroupJoinRequest(account_id="alex",group_id="g1"))
        with self.assertRaises(HTTPException):
            join_group(GroupJoinRequest(account_id="alex",group_id="g1"))
        with self.assertRaises(HTTPException):
            join_group(GroupJoinRequest(account_id="mia",group_id="g3"))
        with self.assertRaises(HTTPException) as ctx:
            decide_group(pending["id"],GroupJoinDecision(account_id="mia",status="accepted"))
        self.assertEqual(ctx.exception.status_code,403)

    def test_capacity_enforced_when_host_accepts(self):
        p1=join_group(GroupJoinRequest(account_id="alex",group_id="g1"))
        p2=join_group(GroupJoinRequest(account_id="mia",group_id="g1"))
        p3=join_group(GroupJoinRequest(account_id="noah",group_id="g1"))
        decide_group(p1["id"],GroupJoinDecision(account_id="joshua",status="accepted"))
        decide_group(p2["id"],GroupJoinDecision(account_id="joshua",status="accepted"))
        with self.assertRaises(HTTPException) as ctx:
            decide_group(p3["id"],GroupJoinDecision(account_id="joshua",status="accepted"))
        self.assertEqual(ctx.exception.status_code,409)
if __name__=="__main__":unittest.main()
