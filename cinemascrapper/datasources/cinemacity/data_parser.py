from ..base import BaseDataParser, DataParseInputError


class CinemaCityDataParser(BaseDataParser):
    def parse(self, input_data, parameters):
        assert isinstance(input_data, dict)

        body = input_data['body']

        if body is None:
            raise DataParseInputError("Body key does not exist in given data object")

        movies = body['films']

        if movies is None:
            raise DataParseInputError("Movies key is not existent in given data")

        parsed_movies = []

        for movie in movies:
            movie_obj = {
                'name': movie['name'],
                'length': movie['length'],
            }

            parsed_movies.append(movie_obj)

        return parsed_movies
