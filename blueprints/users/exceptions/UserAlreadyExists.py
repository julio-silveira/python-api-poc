from dataclasses import dataclass
from infraestructure.exceptions import BadRequestException


@dataclass
class UserAlreadyExistsException(BadRequestException):
    error_code: str = "USER_ALREADY_EXISTS"
    message: str = "User already exists!"
    status_code: int = 409
