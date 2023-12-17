from flask import Flask, jsonify
from marshmallow import ValidationError

from infraestructure.exceptions import HttpException
from infraestructure.response import Response


def init_app(app: Flask):
    @app.errorhandler(ValidationError)
    def handle_validation_error(e: ValidationError):
        response = Response(
            message="Failed to validate the request body",
            error_code="VALIDATION_ERROR",
            status_code=422,
            errors=e.normalized_messages(),
        )
        return response.error()

    @app.errorhandler(HttpException)
    def handle_exception(e: HttpException):
        response = Response(
            message=e.message,
            error_code=e.error_code,
            status_code=e.status_code,
            errors=e.payload,
        )
        return response.error()

    @app.errorhandler(404)
    def handle_not_found(e):
        response = Response(
            message="Resource not found",
            error_code="NOT_FOUND",
            status_code=404,
        )
        return response.error()

    @app.errorhandler(Exception)
    def handle_exception(e: Exception):
        response = Response(
            message="Something went wrong",
            error_code="INTERNAL_SERVER_ERROR",
            status_code=500,
            errors=e.args[0] if e.args else None,
        )
        return response.error()
