from setupdb import db


class UsersFilms(db.Model):
    __tablename__ = 'usersfilms'
    num = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    director = db.relationship("User")
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")

"""

users_films = db.Table('usersfilms',
                     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                     db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'))
                     )
                     
                     """
