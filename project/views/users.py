from flask import request
from flask_restx import abort, Namespace, Resource
from marshmallow import Schema, fields, ValidationError

from project.exceptions import ItemNotFound
from project.helpers import auth_required
from project.service.user import UsersService
from project.setupdb import db

user_ns = Namespace("user")


class UserValidator(Schema):
    password_1 = fields.Str(required=True)
    password_2 = fields.Str(required=True)


@user_ns.route("/")
class UserView(Resource):
    @user_ns.response(200, "OK")
    @user_ns.response(404, "User not found")
    @auth_required
    def get(self, user_id: int):
        """Get user by id"""
        try:
            return UsersService(db.session).get_user_by_id(user_id)
        except ItemNotFound:
            abort(404, message="User not found")

    @user_ns.response(204, "OK")
    @user_ns.response(404, "Ooops")
    @auth_required
    def patch(self, user_id):
        """Update user`s information"""
        req_json = request.json
        try:
            return UsersService(db.session).partially_update(user_id, req_json)
        except ItemNotFound:
            abort(404, message="Error")


@user_ns.route("/password")
class UsersView(Resource):
    @user_ns.response(204, "OK")
    @user_ns.response(404, "Ooops")
    @auth_required
    def put(self, user_id):
        """Update user`s password"""
        req_json = request.json
        try:
            data = UserValidator().load(req_json)
            return UsersService(db.session).update(user_id, data)
        except ValidationError:
            abort(404, message="Error")
