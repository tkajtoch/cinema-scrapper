from ...datasources.cinemacity import (
    CinemaCityDataParser,
    CinemaCityDataSource,
)
from ..base import BaseMovieTheater


class CinemaCityMovieTheater(BaseMovieTheater):
    name = 'cinemacity'
    display_name = 'Cinema City'
    movie_theaters = [
        {
            'city': 'bielskobiala',
            'display_name': 'Bielsko Biała',
            'id': 1088
        },
        {
            'city': 'bydgoszcz',
            'display_name': 'Bydgoszcz',
            'id': 1086
        },
        {
            'city': 'bytom',
            'display_name': 'Bytom',
            'id': 1092
        },
        {
            'city': 'czestochowa',
            'display_name': 'Częstochowa - Galeria Jurajska',
            'id': 1089
        },
        {
            'city': 'czestochowa',
            'display_name': 'Częstochowa - Wolność',
            'id': 1075
        },
    ]
    data_parser = CinemaCityDataParser
    data_source = CinemaCityDataSource
