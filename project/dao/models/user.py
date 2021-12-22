from project.dao.models.base import BaseMixin
from project.setupdb import db


class User(BaseMixin, db.Model):
    __tablename__ = "users"
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(200))
    surname = db.Column(db.String(200))
    favorite_genre = db.Column(db.String(200), db.ForeignKey("genres.id"))
    genre = db.relationship("Genre")
