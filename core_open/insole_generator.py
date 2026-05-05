import math


def _tri(n1, n2, n3):
    return f"facet normal 0 0 0\n outer loop\n  vertex {n1[0]} {n1[1]} {n1[2]}\n  vertex {n2[0]} {n2[1]} {n2[2]}\n  vertex {n3[0]} {n3[1]} {n3[2]}\n endloop\nendfacet\n"


def generate_simple_insole_stl(length_mm: float, width_mm: float, thickness_mm: float, output_path: str) -> None:
    # Elliptical prism approximation with tapered heel
    segments = 48
    top = []
    bottom = []

    for i in range(segments):
        theta = 2 * math.pi * i / segments
        x = (length_mm / 2) * math.cos(theta)
        y_scale = 0.6 + 0.4 * max(0, math.cos(theta))
        y = (width_mm / 2) * math.sin(theta) * y_scale
        top.append((x, y, thickness_mm))
        bottom.append((x, y, 0.0))

    stl = ["solid insole\n"]

    center_top = (0.0, 0.0, thickness_mm)
    center_bottom = (0.0, 0.0, 0.0)

    for i in range(segments):
        j = (i + 1) % segments
        stl.append(_tri(center_top, top[i], top[j]))
        stl.append(_tri(center_bottom, bottom[j], bottom[i]))
        stl.append(_tri(bottom[i], bottom[j], top[j]))
        stl.append(_tri(bottom[i], top[j], top[i]))

    stl.append("endsolid insole\n")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("".join(stl))
