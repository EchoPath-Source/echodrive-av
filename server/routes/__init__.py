from .health import health_bp
from .refine import refine_bp
from .metrics import metrics_bp


def register_blueprints(app):
    app.register_blueprint(health_bp)
    app.register_blueprint(refine_bp)
    app.register_blueprint(metrics_bp)
