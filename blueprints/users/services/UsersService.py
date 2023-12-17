from typing import List
from sqlalchemy import select
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.orm import Session

from blueprints.users.dto.UserDto import UserDto
from blueprints.users.exceptions.NotFoundUser import NotFoundUserException
from database.User import User


class UsersService:
    model: User
    session: Session

    def __init__(self, db: SQLAlchemy):
        self.session = db.session
        self.model = User

    def get_all(self) -> List[User]:
        users = self.session.execute(select(User)).scalars().all()
        return users

    def get_by_id_or_raise(self, id: int) -> User:
        user = self.session.execute(select(User).where(User.id == id)).scalar()

        if not user:
            raise NotFoundUserException()

        return user

    def get_by_username_or_email(self, username: str, email: str) -> User:
        user = self.session.execute(
            select(User).where((User.username == username) | (User.email == email))
        ).scalar()

        return user

    def create(self, data: UserDto) -> User:
        new_user = User(**data.__dict__)

        self.session.add(new_user)
        self.session.commit()

        return new_user

    def update(self, id: int, data: UserDto) -> User:
        user = self.get_by_id_or_raise(id=id)

        user.username = data.username
        user.email = data.email

        self.session.commit()

        return user

    def delete(self, id: int) -> None:
        user = self.get_by_id_or_raise(id=id)

        self.session.delete(user)
        self.session.commit()
