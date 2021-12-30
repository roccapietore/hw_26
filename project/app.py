from flask import Flask
from flask_restx import Api

from project.setupdb import db
from project.views.auth import auth_ns
from project.views.genres import genres_ns
from project.views.directors import directors_ns
from project.views.movies import movies_ns
from project.views.users import user_ns

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
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    return app

