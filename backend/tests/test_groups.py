"""Local demo group workflow regression checks."""
import tempfile
import unittest
from pathlib import Path
from app import requests_store,group_store
from app.main import GroupJoinRequest,GroupJoinDecision,MatchRequest,join_group,decide_group,group_inbox,demo_groups,groups
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

    def test_recommendation_flags_membership(self):
        query=MatchRequest(subject="Mathematics",topic="Quadratic Equations",preferred_slot="Wednesday 3 PM",account_id="alex")
        self.assertEqual(next(g for g in groups(query)["matches"] if g["id"]=="g1")["membership_status"],"")
        pending=join_group(GroupJoinRequest(account_id="alex",group_id="g1"))
        self.assertEqual(next(g for g in groups(query)["matches"] if g["id"]=="g1")["membership_status"],"pending")
        decide_group(pending["id"],GroupJoinDecision(account_id="joshua",status="accepted"))
        self.assertEqual(next(g for g in groups(query)["matches"] if g["id"]=="g1")["membership_status"],"accepted")

    def test_member_directory_permissions(self):
        pending=join_group(GroupJoinRequest(account_id="alex",group_id="g1"))
        with self.assertRaises(HTTPException) as err:
            group_members("g1","alex")
        self.assertEqual(err.exception.status_code,403)
        self.assertEqual(group_members("g1","joshua")["members"][0]["role"],"Host")
        decide_group(pending["id"],GroupJoinDecision(account_id="joshua",status="accepted"))
        self.assertIn("alex",[p["account_id"] for p in group_members("g1","alex")["members"]])
        with self.assertRaises(HTTPException) as err:
            group_members("g1","mia")
        self.assertEqual(err.exception.status_code,403)

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
