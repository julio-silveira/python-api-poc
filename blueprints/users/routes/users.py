from flask import Blueprint, request
from blueprints.users.exceptions.RequiredId import RequiredIdException
from blueprints.users.exceptions.UserAlreadyExists import UserAlreadyExistsException
from blueprints.users.schemas.UserSchema import UserSchema
from blueprints.users.services.UsersService import UsersService
from extensions.database import db
from infraestructure.response import Response
from flasgger import swag_from


bp_users = Blueprint("user", __name__, url_prefix="/users")


@bp_users.get("")
@swag_from("docs/getAll.yml")
def getAll():
    users_service = UsersService(db)
    users = users_service.get_all()

    data = [user.to_dict() for user in users]

    return Response(message="Users retrieved successfully!", data=data).success()


@bp_users.get("/<int:id>")
@swag_from("docs/getOne.yml")
def getById(id: int):
    if not id:
        raise RequiredIdException()

    users_service = UsersService(db)
    user = users_service.get_by_id_or_raise(id)

    return Response(
        message="User retrieved successfully!", data=user.to_dict()
    ).success()


@bp_users.post("")
@swag_from("docs/create.yml")
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
@swag_from("docs/update.yml")
def update(id: int):
    if not id:
        raise RequiredIdException()

    data = request.get_json()
    user_schema = UserSchema()
    user = user_schema.load(data)

    users_service = UsersService(db)
    user = users_service.update(id, user)

    return Response(message="User updated successfully!", data=user.to_dict()).success()


@bp_users.delete("/<int:id>")
@swag_from("docs/delete.yml")
def delete(id: int):
    if not id:
        raise RequiredIdException()

    users_service = UsersService(db)
    users_service.delete(id)

    return Response(message="User deleted successfully!").success()
