from .base.datasource import BaseDataSource
from .cinemacity.datasource import CinemaCityDataSource
from .multikino.datasource import MultiKinoDataSource

data_sources = (
    CinemaCityDataSource,
    MultiKinoDataSource
)
