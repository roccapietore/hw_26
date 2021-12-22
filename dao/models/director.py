from dao.models.base import BaseMixin
from setupdb import db


class Director(BaseMixin, db.Model):
    __tablename__ = "directors"

    name = db.Column(db.String(100), unique=True, nullable=False)
