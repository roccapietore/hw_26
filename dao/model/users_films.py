from setupdb import db


class UsersFilms(db.Model):
    __tablename__ = 'usersfilms'
    num = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    director = db.relationship("User")
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"))
    genre = db.relationship("Genre")

