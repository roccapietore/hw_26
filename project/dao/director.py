from project.dao.base import BaseDao
from project.dao.models import Director


class DirectorDAO(BaseDao):

    def get_by_id(self, pk):
        return self._db_session.query(Director).filter(Director.id == pk).one_or_none()

    def get_all(self):
        return self._db_session.query(Director).all()



