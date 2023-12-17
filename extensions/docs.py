from flasgger import Swagger
from flask import Flask


def init_app(app: Flask):
    Swagger(app)
    return app
