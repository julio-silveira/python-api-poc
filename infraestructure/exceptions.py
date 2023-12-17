from dataclasses import dataclass, field


@dataclass
class HttpException(Exception):
    status_code: int = field(default=500)
    error_code: str = field(default="INTERNAL_SERVER_ERROR")
    message: str = field(default="Something went wrong")
    payload: dict = field(default=None)

    def __post_init__(self):
        Exception.__init__(self)


@dataclass
class BadRequestException(HttpException):
    status_code: int = field(default=400)
    error_code: str = field(default="BAD_REQUEST")
    message: str = field(default="Bad request")
    payload: dict = field(default=None)


@dataclass
class NotFoundException(HttpException):
    status_code: int = field(default=404)
    error_code: str = field(default="NOT_FOUND")
    message: str = field(default="Resource not found")
    payload: dict = field(default=None)
