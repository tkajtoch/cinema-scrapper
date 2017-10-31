from ...datasources.multikino import (
    MultiKinoDataSource,
    MultiKinoDataParser,
)
from ..base import BaseMovieTheater


class MultiKinoMovieTheater(BaseMovieTheater):
    name = 'multikino'
    display_name = 'Multi Kino'
    movie_theaters = [
        {
            'city': 'bydgoszcz',
            'display_name': 'Bydgoszcz',
            'id': 3
        },
        {
            'city': 'czechowicedziedzice',
            'display_name': 'Czechowice-Dziedzice',
            'id': 37
        },
        {
            'city': 'elblag',
            'display_name': 'Elbląg',
            'id': 2
        },
        {
            'city': 'gdansk',
            'display_name': 'Gdańsk',
            'id': 4
        },
        {
            'city': 'gdynia',
            'display_name': 'Gdynia',
            'id': 5
        },
    ]
    data_source = MultiKinoDataSource
    data_parser = MultiKinoDataParser
