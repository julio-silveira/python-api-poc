from marshmallow import Schema, post_load
from marshmallow.fields import Integer, String, Email
from blueprints.users.dto.UserDto import UserDto


class UserSchema(Schema):
    id: int = Integer(required=False, allow_none=True)
    username: str = String(required=True, allow_none=False)
    email: str = Email(required=True, allow_none=False)

    @post_load
    def make_class(self, data, **kwargs):
        return UserDto(**data)
