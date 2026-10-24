import unittest
from app.matching import match_tutors, match_groups

class MatchingTests(unittest.TestCase):
    def test_tutor_eligibility_and_rank(self):
        matches = match_tutors("Mathematics","Quadratic Equations","Wednesday 3 PM",11)
        self.assertEqual(matches[0]["id"],"t1")
        self.assertEqual(matches[0]["score"],100)
        self.assertNotIn("t10",[m["id"] for m in matches])
        self.assertTrue(all(m["subject"]=="Mathematics" for m in matches))
    def test_tutor_topic_and_slot_affect_order(self):
        a=match_tutors("Mathematics","Statistics","Thursday 4 PM",11)
        self.assertEqual(a[0]["id"],"t2")
    def test_groups_exclude_full_and_wrong_subject(self):
        matches=match_groups("Mathematics","Quadratic Equations","Wednesday 3 PM")
        self.assertEqual(matches[0]["id"],"g1")
        self.assertEqual(matches[0]["score"],100)
        self.assertNotIn("g3",[m["id"] for m in matches])
        self.assertTrue(all(m["available_seats"]>0 for m in matches))
    def test_unavailable_tutors_excluded(self):
        matches=match_tutors("Mathematics","Quadratic Equations","Friday 2 PM",11)
        self.assertTrue(all("Friday 2 PM" in m["slots"] for m in matches))
        self.assertNotIn("t3",[m["id"] for m in matches])

    def test_unavailable_groups_excluded(self):
        matches=match_groups("Mathematics","Quadratic Equations","Wednesday 3 PM")
        self.assertTrue(all(m["slot"]=="Wednesday 3 PM" for m in matches))
        self.assertNotIn("g2",[m["id"] for m in matches])

    def test_time_weight_is_largest(self):
        # Existing subject eligibility is mandatory; time is the largest scoring factor.
        a=match_tutors("Mathematics","Statistics","Wednesday 3 PM",12)
        self.assertTrue(all(m["score"]<=100 for m in a))
        self.assertEqual(a[0]["id"],"t2")

    def test_empty_subject(self):
        self.assertEqual(match_tutors("History"),[])
        self.assertEqual(match_groups("History"),[])

if __name__=="__main__":
    unittest.main()
