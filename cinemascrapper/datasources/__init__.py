from .base.datasource import BaseDataSource
from .cinemacity import (
    CinemaCityDataSource,
    CinemaCityDataParser
)
from .multikino import (
    MultiKinoDataSource,
    MultiKinoDataParser
)

data_sources = {
    'cinemacity': {
        'datasource': CinemaCityDataSource,
        'data_parser': CinemaCityDataParser
    },
}
