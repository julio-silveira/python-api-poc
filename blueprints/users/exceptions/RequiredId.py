from dataclasses import dataclass
from infraestructure.exceptions import BadRequestException


@dataclass
class RequiredIdException(BadRequestException):
    error_code: str = "VALIDATION_ERROR"
    message: str = "Id is required!"
    status_code: int = 422
