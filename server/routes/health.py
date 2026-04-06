from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)


@health_bp.get("/")
def root():
    return jsonify({
        "service": "echodrive-av",
        "status": "ok",
        "message": "EchoDrive AV API online"
    })


@health_bp.get("/health")
def health():
    return jsonify({"status": "healthy"})
