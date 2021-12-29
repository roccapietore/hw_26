from sqlalchemy import desc
from project.dao.base import BaseDao
from project.dao.models.movie import Movie


class MovieDAO(BaseDao):
    def get_by_id(self, pk):
        return self._db_session.query(Movie).filter(Movie.id == pk).one_or_none()

    def get_all(self, filters):
        t = self._db_session.query(Movie)
        if "page" in filters:
            t = t.limit(12).offset(12*(filters.page - 1))

        if "status" in filters:
            t = t.order_by(desc(Movie.year))
        return t.all()


