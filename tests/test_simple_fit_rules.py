import unittest

from core_open.input_schema import InsoleInput
from core_open.simple_fit_rules import apply_simple_fit_rules


class TestSimpleFitRules(unittest.TestCase):
    def test_returns_fit_keys(self):
        obj = InsoleInput.from_dict(
            {
                "left_foot_length_mm": 260,
                "right_foot_length_mm": 262,
                "left_forefoot_width_mm": 100,
                "right_forefoot_width_mm": 102,
                "arch_height_level": "medium",
                "instep_pressure_level": "mild",
                "use_case": "standing",
                "in_shoe_space_preference": "thick",
            }
        )
        out = apply_simple_fit_rules(obj)
        self.assertIn("fit_note", out)
        self.assertIn("caution_flags", out)
        self.assertIn("recommended_insole_thickness_mm", out)
