from project.dao.user import UserDAO
from project.exceptions import ItemNotFound
from project.schemas.user import UserSchema
from project.service.base import BaseService


class UsersService(BaseService):
    def get_user_by_id(self, uid):
        user = UserDAO(self._db_session).get_by_id(uid)
        if not user:
            raise ItemNotFound
        return UserSchema().dump(user)

    def partially_update(self, uid, data):
        UserDAO(self._db_session).partially_update(uid, data)
        return UserDAO(self._db_session)

    def update(self, uid, data):
        password_1 = data.get("password_1")
        password_2 = data.get("password_2")
        if password_1 != password_2:
            raise ItemNotFound
        UserDAO(self._db_session).update(uid, data)
        return UserDAO(self._db_session)



