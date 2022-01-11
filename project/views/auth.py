from flask import request
from flask_restx import Resource, Namespace, abort
from marshmallow import Schema, fields, ValidationError

from project.exceptions import ItemNotFound
from project.service.auth import AuthService
from project.setupdb import db

auth_ns = Namespace('auth')


class AuthValidator(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)


@auth_ns.route('/register')
class AuthView(Resource):
    @auth_ns.response(201, "Created")
    @auth_ns.response(404, "Oooops")
    def post(self):
        """Create new user"""
        req_json = request.json
        try:
            data = AuthValidator().load(req_json)
            new_user = AuthService(db.session).create(**data)
            if not new_user:
                return "User with this email have been already registered", 409
            return "", 201
        except ValidationError:
            abort(404, message="Все хорошо, но надо переделать")


@auth_ns.route('/login')
class LoginView(Resource):
    """Get access_token & refresh_token"""
    def post(self):
        req_json = request.json
        try:
            data = AuthValidator().load(req_json)
            tokens = AuthService(db.session).get_user(data)
            return tokens, 201
        except ValidationError:
            abort(404)

    def put(self):
        """Get refresh_token"""
        req_json = request.json
        refresh_token = req_json.get("refresh_token")
        try:
            tokens = AuthService(db.session).get_refresh_token(refresh_token)
            return tokens, 201
        except ItemNotFound:
            abort(404, message="Oooops")

