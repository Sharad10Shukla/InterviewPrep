# Design a online movie booking app
# Identify objects
# Location,MovieTheatre,Screen,Seats,Movie,User,Booking,Payment
# follow up - how to maintain concurrency
from typing import List
class Movie():
    def __init__(self, name, description,year,duration):
        self.name = name
        self.description = description
        self.year_of_release = year
        self.duration = duration


class Location():
    def __init__(self, name, city):
        self.name = name
        self.city = city

class Seat:
    def __init__(self, row,column,seat_type,is_empty:True):
        self.row = row
        self.column = column
        self.seat_type = seat_type
        self.is_empty = is_empty

class SeatManager():
    def __init__(self):
        self.seats = [] #list of seat objects


    def get_empty_seats(self):
        pass

class Screen():
    def __init__(self, number,movie: Movie,start_time,seat: SeatManager):
        self.number = number
        self.movie = movie
        self.start_time = start_time
        self.seat_obj = seat

    def get_empty_seats(self):
        pass

class Theater():
    def __init__(self, screen_list: List[Screen],location: Location):
        self.screens = screen_list # list of screen objects
        self.location = location

    def get_screens(self):
        return self.screens
    def get_movies(self):
        movie_list = []
        for screen in self.screens:
            movie_list.append(screen.movie.name)
        return movie_list


class TheaterManager():
    def __init__(self):
        from collections import defaultdict
        self.theaters = defaultdict(list)
#map of location to theaters

    def add_theater(self, location , theater):
        self.theaters[location].append(theater)

    def show_movies(self,location):
        movie_search_list = []
        for theater in self.theaters[location]:
            movie_search_list.extend(theater.get_movies())
        return movie_search_list

class Booking():
    pass

class Payment():
    pass
class User:
    def __init__(self, name,email):
        self.name = name
        self.email = email
        self.booking = Booking()
    def add_booking(self):
        pass
    def make_payment(self):
        pass

if __name__ == '__main__':
    location_obj1 = Location('Kormangla', 'Bengaluru')
    location_obj2 = Location('Indira_nagar', 'Bengaluru')
    movie1 = Movie('Top Gun Maverick','Action Thriller',2021,120)
    movie2 = Movie('Shaitaan', 'Horror', 2024, 130)
    seat_obj = SeatManager()
    screen_obj1 = Screen(1,movie1,'1800',seat_obj)
    screen_obj2 = Screen(2, movie2, '2100', seat_obj)
    screen_obj2 = Screen(1, movie2, '2200', seat_obj)
    theater1 = Theater([screen_obj1,screen_obj2],location_obj1)
    theater2 = Theater([screen_obj2], location_obj2)
    manager_obj = TheaterManager()
    manager_obj.add_theater(location_obj1,theater1)
    print(manager_obj.show_movies(location_obj1))
    manager_obj2 = TheaterManager()
    manager_obj2.add_theater(location_obj2, theater2)
    print(manager_obj2.show_movies(location_obj2))





















