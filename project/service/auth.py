import jwt
from project.dao.auth import AuthDAO
from project.exceptions import ItemNotFound
from project.service.base import BaseService
from project.tools.security import compare_passwords, generate_password_hash
from flask import current_app
import calendar
import datetime


class AuthService(BaseService):
    def create(self, **user):
        user["password"] = generate_password_hash(user["password"])
        return AuthDAO(self._db_session).create(**user)

    @staticmethod
    def get_tokens(data):
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, key=current_app.config["SECRET_KEY"], algorithm="HS256")

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, key=current_app.config["SECRET_KEY"], algorithm="HS256")
        return {"access_token": access_token, "refresh_token": refresh_token}

    def get_user(self, data):
        user = AuthDAO(self._db_session).get_user(data)
        if not user:
            return ItemNotFound

        compare_passwords_ = compare_passwords(password_hash=user.password, password=data["password"])
        if not compare_passwords_:
            return ItemNotFound

        user_data = {
            "id": user.id,
            "email": user.email
        }
        return self.get_tokens(user_data)

    def get_refresh_token(self, refresh_token):
        try:
            data = jwt.decode(jwt=refresh_token, key=current_app.config["SECRET_KEY"], algorithms="HS256")
            return self.get_tokens(data)
        except ItemNotFound:
            "error"
