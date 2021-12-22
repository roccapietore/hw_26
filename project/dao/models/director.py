from project.dao.models.base import BaseMixin
from project.setupdb import db


class Director(BaseMixin, db.Model):
    __tablename__ = "directors"

    name = db.Column(db.String(100), unique=True, nullable=False)
