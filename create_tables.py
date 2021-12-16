import os

from config import Config
from dao.model.user import User
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.model.users_films import UsersFilms
from app import create_app
from setupdb import db

app = create_app(Config())

with app.app_context():
    db.create_all()

