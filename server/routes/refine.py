from flask import Blueprint, jsonify, request

refine_bp = Blueprint("refine", __name__)


@refine_bp.post("/api/v1/refine-path")
def refine_path_stub():
    payload = request.get_json(silent=True) or {}
    return jsonify({
        "status": "stub",
        "message": "Path refinement endpoint scaffolded. Integrate protected planner logic server-side.",
        "received_keys": sorted(list(payload.keys())),
        "expected_inputs": [
            "path_points",
            "occupancy_map",
            "cost_map",
            "dynamic_obstacles",
            "constraints"
        ]
    })
