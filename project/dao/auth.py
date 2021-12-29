from project.dao.base import BaseDao
from project.dao.models.user import User


class AuthDAO(BaseDao):
    def create(self, new_user):
        user = User(new_user)
        self._db_session.add(user)
        self._db_session.commit()
        return user
