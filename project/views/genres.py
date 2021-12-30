from flask import request
from flask_restx import abort, Namespace, Resource
from project.exceptions import ItemNotFound
from project.service import GenresService
from project.setupdb import db

genres_ns = Namespace("genres")


@genres_ns.route("/")
class GenresView(Resource):
    @genres_ns.response(200, "OK")
    @genres_ns.response(404, "Genres not found")
    def get(self):
        """Get all genres"""
        page = request.args.get("page")
        filters = {"page": page}
        try:
            return GenresService(db.session).get_all_genres(filters)
        except ItemNotFound:
            abort(404, message="Genres not found")


@genres_ns.route("/<int:genre_id>")
class GenreView(Resource):
    @genres_ns.response(200, "OK")
    @genres_ns.response(404, "Genre not found")
    def get(self, genre_id: int):
        """Get genre by id"""
        try:
            return GenresService(db.session).get_item_by_id(genre_id)
        except ItemNotFound:
            abort(404, message="Genre not found")
