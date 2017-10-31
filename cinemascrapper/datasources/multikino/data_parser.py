from datetime import datetime
from ..base import BaseDataParser, DataParseInputError


class MultiKinoDataParser(BaseDataParser):
    def parse(self, input_data, parameters):
        assert isinstance(input_data, dict)

        requested_date = parameters['date']

        movies = input_data['films']

        if movies is None:
            raise DataParseInputError("Movies key does not exist in given data object")

        parsed_movies = []

        for movie in movies:
            showings = movie['showings']
            correct = False

            for showing in showings:
                movie_datetime_str = showing['date_time']
                movie_datetime = datetime.strptime(movie_datetime_str, '%Y-%m-%d')

                if movie_datetime == requested_date:
                    correct = True
                    break

            if not correct:
                continue

            movie_length_str = movie['info_runningtime'].split()
            movie_length = -1

            if len(movie_length_str) == 2:
                try:
                    movie_length = int(movie_length_str[0])
                except ValueError:
                    pass

            movie_obj = {
                'name': movie['title'],
                'length': movie_length
            }

            parsed_movies.append(movie_obj)

        return parsed_movies
