from flask import Blueprint, jsonify, request

from services.motion_metrics import summarize_motion_metrics

metrics_v2_bp = Blueprint("metrics_v2", __name__)


@metrics_v2_bp.post("/api/v1/evaluate-motion-v2")
def evaluate_motion():
    payload = request.get_json(silent=True) or {}
    trajectory = payload.get("trajectory", [])
    baseline_trajectory = payload.get("baseline_trajectory", [])

    response = {
        "status": "ok",
        "received_keys": sorted(list(payload.keys())),
        "trajectory_metrics": summarize_motion_metrics(trajectory),
        "baseline_metrics": summarize_motion_metrics(baseline_trajectory) if baseline_trajectory else None,
        "notes": [
            "Service-layer metrics scaffold active.",
            "Curvature, jerk, and continuity placeholders remain until protected logic is added."
        ]
    }
    return jsonify(response)
