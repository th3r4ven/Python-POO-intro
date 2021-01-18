

class Program:

    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name.title()

    @property
    def likes(self):
        return self._likes

    def give_like(self):
        self._likes += 1

    def __str__(self):  # function responsible for creating an string representation of the object
        return f'{self._name} - {self.year} - {self._likes}'


class Film(Program):

    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):  # function responsible for creating an string representation of the object
        return f'{self._name} - {self.year} - Duration: {self.duration} - Likes: {self._likes}'


class Series(Program):

    def __init__(self, name, year, season):
        super().__init__(name, year)
        self.season = season

    def __str__(self):  # function responsible for creating an string representation of the object
        return f'{self._name} - {self.year} - Seasons: {self.season} - Likes: {self._likes}'


class Playlist:

    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    @property
    def queue(self):
        return self._programs

    @property
    def size(self):
        return len(self._programs)


if __name__ == '__main__':
    avengers = Film('avengers: infinity war', 2018, 160)
    atlanta = Series('atlanta', 2018, 2)
    vikings = Series('Vikings', 2016, 6)
    spiderman = Film('Spider-Man - multiverse', 2021, 170)

    avengers.give_like()
    avengers.give_like()
    spiderman.give_like()
    spiderman.give_like()
    vikings.give_like()
    vikings.give_like()

    films_and_series = [avengers, spiderman, vikings,atlanta]

    weekend_playlist = Playlist('Weekend with my PC, cuz programmers don\'t have a girlfriend', films_and_series)

    for program in weekend_playlist.queue:
        print(program)
