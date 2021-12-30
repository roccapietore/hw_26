import jwt
from project.dao.auth import AuthDAO
from project.dao.models import User
from project.exceptions import ItemNotFound
from project.service.base import BaseService
from project.tools.security import generate_password_digest
from flask import current_app
import calendar
import datetime
from flask_restx import abort


class AuthService(BaseService):
    def create(self, **user):
        user["password"] = generate_password_digest(user.get("password"))
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

    def compare_data(self, data):
        user = self._db_session.query(User).filter(User.email == data["email"]).first()
        if not user or user.password != generate_password_digest(data["password"]):
            return abort(404)

        return self.get_tokens({
            "email": user.email,
            "password": data["password"]
        })

    def get_refresh_token(self, refresh_token):
        try:
            data = jwt.decode(jwt=refresh_token, key=current_app.config["SECRET_KEY"], algorithms="HS256")
            return self.get_tokens(data)
        except ItemNotFound:
            abort(404)
