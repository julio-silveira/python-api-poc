from flask import Flask, jsonify
from extensions import configuration
from blueprints.health import routes as health_routes
from blueprints.users import routes as users_routes


def init_routes(app):
    health_routes.init_app(app)
    users_routes.init_app(app)


def create_app():
    app = Flask(__name__)
    configuration.init_app(app)
    init_routes(app)

    return app
