from project.dao.base import BaseDao
from project.dao.models.user import User


class AuthDAO(BaseDao):
    def create(self, **new_user):
        new_user = User(**new_user)
        self._db_session.add(new_user)
        self._db_session.commit()
        return new_user
