from dataclasses import dataclass, field


@dataclass
class UserDto:
    id: int = field(default=None)
    username: str = field(default_factory=str)
    email: str = field(default_factory=str)
