import requests
from ..base import BaseDataSource


class MultiKinoDataSource(BaseDataSource):
    def connect(self):
        pass

    def close(self):
        pass

    def fetch(self, cinema, date):
        url = MultiKinoDataSource._get_url(cinema)
        resp = requests.get(url)

        return resp.json()

    @staticmethod
    def _get_url(cinema):
        url = 'https://multikino.pl/data/filmswithshowings/{cinema}'

        replacements = {
            'cinema': cinema
        }

        return url.format(**replacements)
