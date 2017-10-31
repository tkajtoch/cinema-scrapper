from ...datasources.base import (
    BaseDataSource,
    BaseDataParser
)


class BaseMovieTheater(object):
    name = ''
    display_name = ''
    movie_theaters = []
    data_source = BaseDataSource
    data_parser = BaseDataParser
