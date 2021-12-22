from project.dao.models.base import BaseMixin
from project.setupdb import db


class Movie(BaseMixin, db.Model):
    __tablename__ = "movies"

    name = db.Column(db.String(100), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    trailer = db.Column(db.String(200), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("directors.id"))
    director = db.relationship("Director")
