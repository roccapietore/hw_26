from flask import Flask
from flask_restx import Api

from setupdb import db
from views.genres import genres_ns
from views.directors import directors_ns
from views.movies import movies_ns


api = Api(
    authorizations={
        "Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}
    },
    title="Flask Course Project 3",
    doc="/docs",
)


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    db.init_app(app)
    api.init_app(app)

    api.add_namespace(genres_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(movies_ns)

    return app

