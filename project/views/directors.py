from flask import request
from flask_restx import abort, Namespace, Resource
from project.exceptions import ItemNotFound
from project.service.director import DirectorsService
from project.setupdb import db

directors_ns = Namespace("directors")


@directors_ns.route("/")
class DirectorsView(Resource):
    @directors_ns.response(200, "OK")
    @directors_ns.response(404, "Directors not found")
    def get(self):
        """Get all directors"""
        page = request.args.get("page")
        filters = {"page": page}
        try:
            return DirectorsService(db.session).get_all_directors(filters)
        except ItemNotFound:
            abort(404, message="Directors not found")


@directors_ns.route("/<int:director_id>")
class DirectorView(Resource):
    @directors_ns.response(200, "OK")
    @directors_ns.response(404, "Director not found")
    def get(self, director_id: int):
        """Get director by id"""
        try:
            return DirectorsService(db.session).get_item_by_id(director_id)
        except ItemNotFound:
            abort(404, message="Director not found")
