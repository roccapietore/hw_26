from marshmallow import Schema, fields
from setupdb import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, required=True)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False, required=True)
    name = db.Column(db.String(200))
    surname = db.Column(db.String(200))
    favorite_genre = db.Column(db.String(200), db.ForeignKey("genres.id"))
    genre = db.relationship("Genre")


class UserSchema(Schema):
    username = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
