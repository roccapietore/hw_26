from project.config import choose_config
from project.dao.models import User
from project.dao.models import Movie
from project.dao.models import Director
from project.dao.models import Genre
from project.app import create_app, db

app = create_app(choose_config())


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
        "Director": Director,
        "Movie": Movie,
        "User": User
    }
