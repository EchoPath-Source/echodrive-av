from flask import Blueprint, jsonify, request

metrics_bp = Blueprint("metrics", __name__)


@metrics_bp.post("/api/v1/evaluate-motion")
def evaluate_motion_stub():
    payload = request.get_json(silent=True) or {}
    return jsonify({
        "status": "stub",
        "message": "Motion evaluation endpoint scaffolded. Add jerk, curvature, stability, and continuity metrics here.",
        "received_keys": sorted(list(payload.keys())),
        "expected_inputs": [
            "trajectory",
            "time_series",
            "baseline_trajectory",
            "scenario_metadata"
        ],
        "candidate_metrics": [
            "mean_jerk",
            "mean_curvature",
            "max_curvature",
            "replan_stability",
            "tube_persistence",
            "id_continuity",
            "split_merge_rate"
        ]
    })
