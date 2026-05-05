from core_open.input_schema import InsoleInput


def apply_simple_fit_rules(data: InsoleInput) -> dict:
    caution_flags = []
    avg_length = (data.left_foot_length_mm + data.right_foot_length_mm) / 2
    avg_width = (data.left_forefoot_width_mm + data.right_forefoot_width_mm) / 2

    thickness_map = {"thin": 2.0, "medium": 3.5, "thick": 5.0}
    thickness = thickness_map[data.in_shoe_space_preference]

    if data.instep_pressure_level in {"moderate", "high"} and thickness > 3.5:
        caution_flags.append("High instep pressure may feel tight with thicker insoles.")
        thickness = 3.5

    if abs(data.left_foot_length_mm - data.right_foot_length_mm) > 8:
        caution_flags.append("Left/right foot length differs notably; review sizing before printing.")

    if avg_width / avg_length > 0.5:
        caution_flags.append("Forefoot appears wide relative to length; verify in-shoe space.")

    fit_note = "General comfort-oriented placeholder fit for personal experimentation."
    if data.use_case == "standing":
        fit_note = "Standing use selected; consider testing multiple thickness versions."

    return {
        "fit_note": fit_note,
        "caution_flags": caution_flags,
        "recommended_insole_thickness_mm": thickness,
    }
