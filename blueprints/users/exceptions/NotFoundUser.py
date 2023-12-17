from dataclasses import dataclass
from infraestructure.exceptions import NotFoundException


@dataclass
class NotFoundUserException(NotFoundException):
    error_code: str = "NOT_FOUND_USER"
    message: str = "User not found!"
