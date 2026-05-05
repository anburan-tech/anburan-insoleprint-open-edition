import unittest

from core_open.print_readiness import estimate_print_readiness


class TestPrintReadiness(unittest.TestCase):
    def test_ready(self):
        out = estimate_print_readiness(260, 100, 3.5)
        self.assertEqual(out["readiness_status"], "ready")

    def test_not_recommended_size(self):
        out = estimate_print_readiness(340, 100, 3.5)
        self.assertEqual(out["readiness_status"], "not_recommended")
