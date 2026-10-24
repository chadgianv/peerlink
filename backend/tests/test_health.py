"""Unit test for the Phase 0 health endpoint (no external test client needed)."""
import unittest
from app.main import health

class HealthTests(unittest.TestCase):
    def test_health_reports_ready(self):
        self.assertEqual(health()["status"], "ok")
        self.assertEqual(health()["phase"], "2")

if __name__ == "__main__":
    unittest.main()
