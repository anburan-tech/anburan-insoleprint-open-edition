import unittest

from core_open.input_schema import InsoleInput


class TestInputSchema(unittest.TestCase):
    def test_valid_input(self):
        payload = {
            "left_foot_length_mm": 250,
            "right_foot_length_mm": 252,
            "left_forefoot_width_mm": 95,
            "right_forefoot_width_mm": 96,
            "arch_height_level": "low",
            "instep_pressure_level": "none",
            "use_case": "indoor",
            "in_shoe_space_preference": "thin",
        }
        obj = InsoleInput.from_dict(payload)
        self.assertEqual(obj.arch_height_level, "low")

    def test_invalid_input(self):
        payload = {
            "left_foot_length_mm": -1,
            "right_foot_length_mm": 252,
            "left_forefoot_width_mm": 95,
            "right_forefoot_width_mm": 96,
            "arch_height_level": "low",
            "instep_pressure_level": "none",
            "use_case": "indoor",
            "in_shoe_space_preference": "thin",
        }
        with self.assertRaises(ValueError):
            InsoleInput.from_dict(payload)
