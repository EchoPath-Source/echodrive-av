from flask import Flask, jsonify, request


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def root():
        return jsonify({
            "service": "echodrive-av",
            "status": "ok",
            "message": "EchoDrive AV API online"
        })

    @app.get("/health")
    def health():
        return jsonify({"status": "healthy"})

    @app.post("/api/v1/refine-path")
    def refine_path_stub():
        payload = request.get_json(silent=True) or {}
        return jsonify({
            "status": "stub",
            "message": "Path refinement endpoint scaffolded. Integrate protected planner logic server-side.",
            "received_keys": sorted(list(payload.keys()))
        })

    @app.post("/api/v1/evaluate-motion")
    def evaluate_motion_stub():
        payload = request.get_json(silent=True) or {}
        return jsonify({
            "status": "stub",
            "message": "Motion evaluation endpoint scaffolded. Add jerk / curvature / stability metrics here.",
            "received_keys": sorted(list(payload.keys()))
        })

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
