from extensions import database, docs


def init_app(app):
    database.init_app(app)
    docs.init_app(app)

    return app
