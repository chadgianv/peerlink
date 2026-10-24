"""Regression tests for the fictional two-account tutoring workflow."""
import tempfile
import unittest
from pathlib import Path
from fastapi import HTTPException
from app import requests_store
from app.main import TutoringRequest, TutorDecision, submit_tutoring, list_tutoring, respond_tutoring

class RequestFlowTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.original=requests_store.DB_PATH
        requests_store.DB_PATH=Path(self.tmp.name)/"requests.sqlite3"

    def tearDown(self):
        requests_store.DB_PATH=self.original
        self.tmp.cleanup()

    def test_alex_requests_and_joshua_accepts(self):
        created=submit_tutoring(TutoringRequest(learner_id="alex",tutor_id="t1",subject="Mathematics",topic="Quadratic Equations",preferred_slot="Wednesday 3 PM"))
        self.assertEqual(created["status"],"pending")
        self.assertEqual(len(list_tutoring("joshua")["requests"]),1)
        self.assertEqual(len(list_tutoring("alex")["requests"]),1)
        self.assertEqual(len(list_tutoring("mia")["requests"]),0)
        accepted=respond_tutoring(created["id"],TutorDecision(account_id="joshua",status="accepted"))
        self.assertEqual(accepted["status"],"accepted")
        self.assertEqual(list_tutoring("alex")["requests"][0]["status"],"accepted")
        with self.assertRaises(HTTPException) as err:
            respond_tutoring(created["id"],TutorDecision(account_id="joshua",status="declined"))
        self.assertEqual(err.exception.status_code,409)

    def test_non_tutor_cannot_decide(self):
        created=submit_tutoring(TutoringRequest(learner_id="alex",tutor_id="t1",subject="Mathematics",topic="Algebra",preferred_slot="Wednesday 3 PM"))
        with self.assertRaises(HTTPException) as err:
            respond_tutoring(created["id"],TutorDecision(account_id="alex",status="accepted"))
        self.assertEqual(err.exception.status_code,403)

    def test_all_eligible_tutors_and_mismatch_rejected(self):
        sent=submit_tutoring(TutoringRequest(learner_id="alex",tutor_id="t3",subject="Mathematics",preferred_slot="Wednesday 3 PM"))
        self.assertEqual(list_tutoring("mark")["requests"][0]["id"],sent["id"])
        self.assertEqual(respond_tutoring(sent["id"],TutorDecision(account_id="mark",status="accepted"))["status"],"accepted")
        with self.assertRaises(HTTPException):
            submit_tutoring(TutoringRequest(learner_id="alex",tutor_id="t10",subject="Mathematics",preferred_slot="Wednesday 3 PM"))
        with self.assertRaises(HTTPException):
            submit_tutoring(TutoringRequest(learner_id="alex",tutor_id="t1",subject="Mathematics",preferred_slot="Thursday 4 PM"))

if __name__=="__main__":
    unittest.main()
