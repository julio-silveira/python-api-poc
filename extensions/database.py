import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database.BaseClass import Base
from core.settings import settings

db = SQLAlchemy(model_class=Base)


def init_app(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = settings.SQLALCHEMY_DATABASE_URI
    db.init_app(app)
    return app
