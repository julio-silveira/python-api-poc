from dataclasses import dataclass, field
import json


@dataclass
class Response:
    status_code: int = field(default=200)
    message: str = field(default_factory=str)
    data: list | dict | str = field(default=None)
    error_code: str = field(default=None)
    errors: list | dict | str = field(default=None)

    def error(self):
        response = {
            "success": False,
            "message": self.message,
            "error_code": self.error_code,
        }
        if self.errors:
            response["errors"] = self.errors
        return (
            json.dumps(response, sort_keys=False),
            self.status_code,
            {"Content-Type": "application/json"},
        )

    def success(self):
        response = {
            "success": True,
            "message": self.message,
        }
        if self.data:
            response["data"] = self.data
        return (
            json.dumps(response, sort_keys=False),
            self.status_code,
            {"Content-Type": "application/json"},
        )
