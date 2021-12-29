from project.dao.movie import MovieDAO
from project.exceptions import ItemNotFound
from project.schemas.movie import MovieSchema
from project.service.base import BaseService


class MoviesService(BaseService):
    def get_item_by_id(self, pk):
        movie = MovieDAO(self._db_session).get_by_id(pk)
        if not movie:
            raise ItemNotFound
        return MovieSchema().dump(movie)

    def get_all_movies(self, filters):

        if filters.get("page") is not None:
            movies = MovieDAO(self._db_session).get_all(filters.get("page"))
        elif filters.get("status") is not None:
            movies = MovieDAO(self._db_session).get_all(filters.get("status"))
        else:
            movies = MovieDAO(self._db_session).get_all()
        if not movies:
            raise ItemNotFound
        return MovieSchema(many=True).dump(movies)
