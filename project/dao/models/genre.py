from project.dao.models.base import BaseMixin
from project.setupdb import db


class Genre(BaseMixin, db.Model):
    __tablename__ = "genres"

    name = db.Column(db.String(100), unique=True, nullable=False)
