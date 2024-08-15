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

class MovieController():
    _movies = {}
    def __init__(self):
        pass
    def add_movies(self,movie: Movie,city):
        if not MovieController._movies.get(city.city):
            MovieController._movies[city.city] = []
        MovieController._movies[city.city].append(movie)

    def get_movies_by_city(self,city):
        return MovieController._movies[city.city]

class Location():
    def __init__(self, name, city):
        self.name = name
        self.city = city

class Seat:
    def __init__(self, number,row,seat_type,is_empty:True):
        self.number = number
        self.row = row
        self.seat_type = seat_type
        self.is_empty = is_empty

class Show():
    def __init__(self, movie: Movie,start_time,screen, booked_seats: List[Seat]=[]):
        self.booked_seats = booked_seats
        self.movie = movie
        self.start_time = start_time
        self.screen = screen

    def get_empty_seats(self):
        pass

class Screen():
    # _seat = [None,None,None,None]
    def __init__(self, number,seat_list):
        self.number = number
        self.seat = seat_list

    def get_empty_seats(self):
        pass


class Theater():
    def __init__(self,name: str, screen_list: List[Screen],location: Location,show_list):
        self.screens = screen_list # list of screen objects
        self.location = location
        self.name = name
        self.show_list = show_list

    def get_screens(self):
        return self.screens

    def get_movies(self):
        pass


class TheaterManager():
    from typing import Dict
    _theaters: Dict = {}
    def __init__(self):
        pass
# map of location to theaters

    def add_theater(self, city: Location , theater:Theater):
        if not TheaterManager._theaters.get(city.city):
            TheaterManager._theaters[city.city] = []
        TheaterManager._theaters[city.city].append(theater)

    def get_shows(self,city:Location,movie: Movie):
        movie_shows = {}
        for theater in TheaterManager._theaters[city.city]:
            for show in theater.show_list:
                if show.movie.name == movie.name:
                    # print(vars(theater))
                    if theater.name not in movie_shows:
                        movie_shows[theater.name] = []
                    movie_shows[theater.name].append(show)

        return movie_shows

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
    # given a city show me movies in the city.
    mov_cont_obj = MovieController()
    mov_cont_obj.add_movies(movie1,location_obj1)
    mov_cont_obj.add_movies(movie2, location_obj2)
    movie_list = mov_cont_obj.get_movies_by_city(location_obj1)
    seat_obj1 = Seat(1,"A","Premium",True)
    seat_list = [seat_obj1]
    Screen_obj = Screen(1,seat_list)
    show1 = Show(movie1,"1900",Screen_obj,[])
    th_obj = Theater("PVR",[Screen_obj],location_obj1,[show1])
    # given a movie find shows in the city
    the_mngr = TheaterManager()
    the_mngr.add_theater(location_obj1,th_obj)
    shows = the_mngr.get_shows(location_obj1,movie1)
    for key ,val in shows.items():
        for v in val:
            print(key,vars(v))

    # for m in movie_list:
    #     print(vars(m))
    # seat_obj = SeatManager()
    # screen_obj1 = Screen(1,movie1,'1800',seat_obj)
    # screen_obj2 = Screen(2, movie2, '2100', seat_obj)
    # screen_obj2 = Screen(1, movie2, '2200', seat_obj)
    # theater1 = Theater([screen_obj1,screen_obj2],location_obj1)
    # theater2 = Theater([screen_obj2], location_obj2)
    # manager_obj = TheaterManager()
    # manager_obj.add_theater(location_obj1,theater1)
    # print(manager_obj.show_movies(location_obj1))
    # manager_obj2 = TheaterManager()
    # manager_obj2.add_theater(location_obj2, theater2)
    # print(manager_obj2.show_movies(location_obj2))





















