from project.dao.base import BaseDao
from project.dao.models.user import User
from project.exceptions import ItemNotFound


class AuthDAO(BaseDao):
    def create(self, **new_user):
        self._db_session.query(User).filter(User.email == new_user["email"]).first()
        new_user = User(**new_user)
        if not new_user:
            return ItemNotFound
        self._db_session.add(new_user)
        self._db_session.commit()
        return new_user

    def get_user(self, data):
        user = self._db_session.query(User).filter(User.email == data["email"]).first()
        return user
