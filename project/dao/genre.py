from project.dao.base import BaseDao
from project.dao.models import Genre


class GenreDAO(BaseDao):

    def get_by_id(self, pk):
        return self._db_session.query(Genre).filter(Genre.id == pk).one_or_none()

    def get_all(self, filters):
        t = self._db_session.query(Genre)
        if filters["page"]:
            t = t.limit(12).offset((int(filters.get("page")) - 1) * 12)
        return t.all()

