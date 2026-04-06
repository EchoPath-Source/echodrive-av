from flask import Blueprint, jsonify, request

from services.refine_service import refine_path

refine_v2_bp = Blueprint("refine_v2", __name__)


@refine_v2_bp.post("/api/v1/refine-path-v2")
def refine_path_endpoint():
    payload = request.get_json(silent=True) or {}
    path_points = payload.get("path_points", [])
    constraints = payload.get("constraints", {})

    response = refine_path(path_points=path_points, constraints=constraints)
    response["received_keys"] = sorted(list(payload.keys()))
    return jsonify(response)
