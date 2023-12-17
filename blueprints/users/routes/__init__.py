from flask import Flask
from blueprints.users.routes.users import bp_users


def init_app(app: Flask):
    app.register_blueprint(bp_users)
