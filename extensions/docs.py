from flasgger import Swagger
from flask import Flask


def init_app(app: Flask):
    template = {
        "swagger": "2.0",
        "info": {
            "title": "Python Flask API",
            "description": "Flask API with Swagger",
        },
    }

    Swagger(app, template=template)
    return app
