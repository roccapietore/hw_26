from dao.models.base import BaseMixin
from setupdb import db


class UsersFilms(BaseMixin, db.Model):

    __tablename__ = 'usersfilms'
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    director = db.relationship("User")
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"))
    genre = db.relationship("Genre")

