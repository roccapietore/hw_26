from config import DevelopmentConfig
from app import create_app
from setupdb import db
from dao.model import *

app = create_app(DevelopmentConfig())

with app.app_context():
    db.drop_all()
    db.create_all()



