import jwt
from flask import request, current_app
from flask_restx import abort


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            user = jwt.decode(token, key=current_app.config["SECRET_KEY"], algorithm="HS256")
            return func(*args, **kwargs, user_id=user["id"])
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
    return wrapper


