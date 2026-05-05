import argparse
import json

from core_open.input_schema import InsoleInput
from core_open.insole_generator import generate_simple_insole_stl
from core_open.print_readiness import estimate_print_readiness
from core_open.simple_fit_rules import apply_simple_fit_rules


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate basic insole STL and summary output.")
    parser.add_argument("--input", required=True, help="Path to input JSON")
    parser.add_argument("--output", required=True, help="Path to output JSON")
    parser.add_argument("--stl", required=True, help="Path to output STL")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        payload = json.load(f)

    model = InsoleInput.from_dict(payload)

    fit = apply_simple_fit_rules(model)
    avg_length = (model.left_foot_length_mm + model.right_foot_length_mm) / 2
    avg_width = (model.left_forefoot_width_mm + model.right_forefoot_width_mm) / 2

    generate_simple_insole_stl(
        length_mm=avg_length,
        width_mm=avg_width,
        thickness_mm=fit["recommended_insole_thickness_mm"],
        output_path=args.stl,
    )

    readiness = estimate_print_readiness(
        length_mm=avg_length,
        width_mm=avg_width,
        thickness_mm=fit["recommended_insole_thickness_mm"],
    )

    output = {
        "input_summary": {
            "avg_foot_length_mm": avg_length,
            "avg_forefoot_width_mm": avg_width,
            "arch_height_level": model.arch_height_level,
            "use_case": model.use_case,
        },
        "fit": fit,
        "print_readiness": readiness,
        "stl_path": args.stl,
        "disclaimer": "Non-medical exploratory output for personal 3D printing experimentation.",
    }

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"Generated STL: {args.stl}")
    print(f"Readiness: {readiness['readiness_status']} ({readiness['estimated_print_minutes']} min est.)")


if __name__ == "__main__":
    main()
