from marshmallow import Schema, fields
from setupdb import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    favorite_genre = db.Column(db.String, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")


class UserSchema(Schema):
    username = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
