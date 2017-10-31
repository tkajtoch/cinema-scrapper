import requests
from ..base import BaseDataSource


class CinemaCityDataSource(BaseDataSource):
    name = 'cinemacity'
    display_name = 'Cinema City'

    def connect(self):
        pass

    def close(self):
        pass

    def fetch(self, cinema, date):
        url = CinemaCityDataSource._get_url(cinema, date)
        print("Requesting: %s" % url)
        resp = requests.get(url)

        return resp.json()

    @staticmethod
    def _get_url(cinema, date):
        base_url = 'https://www.cinema-city.pl/pl/data-api-service/v1/quickbook/10103/film-events/in-cinema/{' \
                   'cinema}/at-date/{date_year}-{date_month}-{date_day}'

        replacements = {
            'cinema': cinema,
            'date_year': date.year,
            'date_month': str(date.month).zfill(2),
            'date_day': str(date.day).zfill(2)
        }

        return base_url.format(**replacements)
