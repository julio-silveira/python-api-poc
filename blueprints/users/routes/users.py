from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from blueprints.users.exceptions.UserAlreadyExists import UserAlreadyExistsException
from blueprints.users.schemas.UserSchema import UserSchema
from blueprints.users.services.UsersService import UsersService
from extensions.database import db
from infraestructure.response import Response


bp_users = Blueprint("user", __name__, url_prefix="/users")


@bp_users.get("/")
def getAll():
    users_service = UsersService(db)
    users = users_service.get_all()

    data = [user.to_dict() for user in users]

    return Response(message="Users retrieved successfully!", data=data).success()


@bp_users.get("/<int:id>")
def getById(id: int):
    if not id:
        raise ValidationError("Id is required!")

    users_service = UsersService(db)
    user = users_service.get_by_id_or_raise(id)

    return Response(
        message="User retrieved successfully!", data=user.to_dict()
    ).success()


@bp_users.post("/")
def create():
    data = request.get_json()
    user_schema = UserSchema()
    user = user_schema.load(data)

    users_service = UsersService(db)

    is_registered = users_service.get_by_username_or_email(user.username, user.email)

    if is_registered:
        raise UserAlreadyExistsException()

    user = users_service.create(user)

    return Response(
        message="User created successfully!", data=user.to_dict(), status_code=201
    ).success()


@bp_users.put("/<int:id>")
def update(id: int):
    data = request.get_json()
    user_schema = UserSchema()
    user = user_schema.load(data)

    users_service = UsersService(db)
    user = users_service.update(id, user)

    return Response(message="User updated successfully!", data=user.to_dict()).success()


@bp_users.delete("/<int:id>")
def delete(id: int):
    if not id:
        raise ValidationError("Id is required!")

    users_service = UsersService(db)
    users_service.delete(id)

    return Response(message="User deleted successfully!").success()
