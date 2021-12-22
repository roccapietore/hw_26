from sqlalchemy.exc import IntegrityError
from config import DevelopmentConfig
from dao.models.genre import Genre
from dao.models.movie import Movie
from dao.models.director import Director
from app import create_app
from setupdb import db
from utils import read_json

app = create_app(DevelopmentConfig)
data = read_json("data.json")

with app.app_context():

    for genre in data["genres"]:
        db.session.add(Genre(id=genre["pk"], name=genre["name"]))
    try:
        db.session.commit()
    except IntegrityError:
        print("Fixtures already loaded")

    for director in data["directors"]:
        db.session.add(Director(id=director["pk"], name=director["name"]))
    try:
        db.session.commit()
    except IntegrityError:
        print("Fixtures already loaded")

    for movie in data["movies"]:
        db.session.add(Movie(title_=director["title"], description=director["description"],
                             trailer=director["trailer"], year=director["year"], rating=director["rating"],
                             genre_id=director["genre_id"],  director_id=director["director_id"], id=director["pk"],))
    try:
        db.session.commit()
    except IntegrityError:
        print("Fixtures already loaded")
