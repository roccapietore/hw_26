from project.dao.base import BaseDao
from project.dao.models.user import User
from project.tools.security import generate_password_hash


class UserDAO(BaseDao):

    def get_by_id(self, uid):
        return self._db_session.query(User).filter(User.id == uid).one_or_none()

    def partially_update(self, uid, user):
        updated_user = self.get_by_id(uid)

        updated_user.name = user.get("name")
        updated_user.surname = user.get("surname")
        updated_user.favorite_genre = user.get("favorite_genre")

        self._db_session.add(updated_user)
        self._db_session.commit()

    def update(self, uid, data):
        updated_user = self.get_by_id(uid)

        if "password_1" in data:
            updated_user.password = generate_password_hash(data.get("password_1"))

        self._db_session.add(updated_user)
        self._db_session.commit()

