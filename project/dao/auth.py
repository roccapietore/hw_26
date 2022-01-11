from project.dao.base import BaseDao
from project.dao.models.user import User
from project.exceptions import ItemNotFound


class AuthDAO(BaseDao):
    def create(self, **new_user):
        try:
            same_user = self._db_session.query(User).filter(User.email == new_user["email"]).first()
            if same_user:
                raise ItemNotFound
            new_user = User(**new_user)
            self._db_session.add(new_user)
            self._db_session.commit()
            return new_user
        except ItemNotFound:
            "error"
    def get_user(self, data):
        user = self._db_session.query(User).filter(User.email == data["email"]).first()
        return user
