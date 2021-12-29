from flask import request
from flask_restx import Resource, Namespace, abort
from marshmallow import Schema, fields, ValidationError

from project.exceptions import ItemNotFound
from project.service.auth import AuthService

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
            user = AuthService.create(req_json)
            return "", 201, {"location": f"/users/{user.id}"}
        except ItemNotFound:
            abort(404, "Oooops")



"""
@auth_ns.route('/login')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        try:
            data = AuthValidator().load(req_json)
            tokens = AuthService.get_tokens(data)
            return tokens, 201
        except ValidationError:
            abort(404)

    def put(self):
        req_json = request.json
        refresh_token = req_json.get("refresh_token")
        if refresh_token is None:
            abort(404)
        tokens = AuthService.get_refresh_token(refresh_token)
        return tokens, 201

"""