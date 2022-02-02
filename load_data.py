from sqlalchemy.exc import IntegrityError
from project.config import choose_config
from project.dao.models.genre import Genre
from project.dao.models.movie import Movie
from project.dao.models.director import Director
from project.app import create_app
from project.setupdb import db
from project.utils import read_json

app = create_app(choose_config())
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
        db.session.add(Movie(id=movie["pk"], title=movie["title"], description=movie["description"],
                             trailer=movie["trailer"], year=movie["year"], rating=movie["rating"],
                             genre_id=movie["genre_id"],  director_id=movie["director_id"]))
    try:
        db.session.commit()
    except IntegrityError:
        print("Fixtures already loaded")
