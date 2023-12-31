from extensions import database, docs, errors


def init_app(app):
    database.init_app(app)
    docs.init_app(app)
    errors.init_app(app)

    return app
