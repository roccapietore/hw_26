from marshmallow import Schema, fields
from setupdb import db


class User(db.Model):
    __tablename__ = 'user'
    email = db.Column(db.String)
    password = db.Column(db.String)
    name = db.Column(db.String)
    surname = db.Column(db.String)


class UserSchema(Schema):
    username = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
