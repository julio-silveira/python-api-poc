from flask import Flask
from blueprints.health.routes.health import bp_health


def init_app(app: Flask):
    app.register_blueprint(bp_health)
