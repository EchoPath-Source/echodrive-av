from typing import Iterable, Sequence

from .motion_metrics import summarize_motion_metrics

Point = Sequence[float]


def refine_path(path_points: Iterable[Point], constraints: dict | None = None) -> dict:
    points = list(path_points or [])
    constraints = constraints or {}

    # Placeholder: return the incoming path until protected refinement logic is added.
    refined_path = points

    return {
        "status": "stub",
        "refined_path": refined_path,
        "constraints_applied": constraints,
        "metrics": summarize_motion_metrics(refined_path),
        "notes": [
            "Protected path refinement logic not yet connected.",
            "Current scaffold echoes the input path and returns placeholder metrics."
        ]
    }
