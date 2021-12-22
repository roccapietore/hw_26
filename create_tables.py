from config import DevelopmentConfig
from dao.models import *
from app import create_app
from setupdb import db

app = create_app(DevelopmentConfig)

with app.app_context():
    db.drop_all()
    db.create_all()

