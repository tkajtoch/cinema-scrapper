#!/usr/bin/env python3

"""
Cinema showtime scrapper

Author: Tomasz Kajtoch <tomek@kajto.ch>
"""

from datetime import datetime
from cinemascrapper.movietheaters import movie_theaters


date = datetime(2017, 11, 1)


def main():
    cities = {}
    theaters_by_name = {}

    for movie_theater in movie_theaters:
        instance = movie_theater()
        theaters_by_name[instance.name] = instance

        for theater in instance.movie_theaters:
            city = theater['city']

            if city in cities:
                cities[city]['id'][instance.name] = theater['id']
            else:
                id = {}
                id[instance.name] = theater['id']

                cities[city] = {
                    'city': city,
                    'display_name': theater['display_name'],
                    'id': id
                }

    for index, city in enumerate(cities.values()):
        display_name = city['display_name']
        number_of_theaters = len(city['id'])

        print("%i\t%s\t\t\t(%i movie theater(s))" % (index, display_name, number_of_theaters))

    max_index = len(cities) - 1

    while True:
        selected_raw = input("Please select the city: ")

        try:
            selected_index = int(selected_raw)

            if selected_index <= max_index:
                break
            else:
                print("You must select a value between 0 and %i" % max_index)
        except ValueError:
            pass

    selected_city = list(cities.values())[selected_index]

    movies = {}

    for theater_name, cinema_id in selected_city['id'].items():
        print("Fetching data for theater: %s" % theater_name)

        instance = theaters_by_name[theater_name]

        ds = instance.data_source()
        dp = instance.data_parser()

        ds.connect()
        parameters = {
            'cinema': cinema_id,
            'date': date,
        }

        raw_data = ds.fetch(**parameters)
        parsed_data = dp.parse(raw_data, parameters)

        for m in parsed_data:
            name = m['name']

            if name in movies.keys():
                movies[name]['theaters'].append(theater_name)
            else:
                movies[name] = {
                    'name': name,
                    'theaters': [
                        theater_name,
                    ]
                }

    for index, movie in enumerate(movies.values()):
        print("%i\t%s\t\t\t\t\t\t(%s)" % (index + 1, movie['name'], ', '.join(movie['theaters'])))

if __name__ == "__main__":
    main()
