from typing import Iterable, Sequence


Point = Sequence[float]


def path_length(points: Iterable[Point]) -> float:
    pts = list(points)
    if len(pts) < 2:
        return 0.0
    total = 0.0
    for i in range(1, len(pts)):
        dx = float(pts[i][0]) - float(pts[i - 1][0])
        dy = float(pts[i][1]) - float(pts[i - 1][1])
        total += (dx * dx + dy * dy) ** 0.5
    return round(total, 6)


def summarize_motion_metrics(trajectory: Iterable[Point]) -> dict:
    pts = list(trajectory)
    return {
        "path_length": path_length(pts),
        "point_count": len(pts),
        "mean_jerk": None,
        "mean_curvature": None,
        "max_curvature": None,
        "replan_stability": None,
        "tube_persistence": None,
        "id_continuity": None,
        "split_merge_rate": None,
        "notes": "Scaffold metrics summary. Replace placeholders with protected implementation."
    }
