def estimate_print_readiness(length_mm: float, width_mm: float, thickness_mm: float) -> dict:
    volume_est_mm3 = length_mm * width_mm * thickness_mm * 0.55
    estimated_print_minutes = int(max(30, volume_est_mm3 / 180))

    if thickness_mm < 2.0:
        return {
            "estimated_print_minutes": estimated_print_minutes,
            "readiness_status": "review",
            "reason": "Very thin model may be fragile depending on material and infill.",
        }

    if length_mm > 330 or width_mm > 140:
        return {
            "estimated_print_minutes": estimated_print_minutes,
            "readiness_status": "not_recommended",
            "reason": "Model may exceed common personal printer build area.",
        }

    return {
        "estimated_print_minutes": estimated_print_minutes,
        "readiness_status": "ready",
        "reason": "Looks suitable for basic personal 3D printing assumptions.",
    }
