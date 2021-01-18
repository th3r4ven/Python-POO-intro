

class Film:

    def __init__(self, name, year, duration):
        self.__name = name.title()
        self.year = year
        self.duration = duration
        self.__likes = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name.title()

    @property
    def likes(self):
        return self.__likes

    def give_like(self):
        self.__likes += 1


class Series:

    def __init__(self, name, year, season):
        self.__name = name.title()
        self.year = year
        self.season = season
        self.__likes = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name.title()

    @property
    def likes(self):
        return self.__likes

    def give_like(self):
        self.__likes += 1


if __name__ == '__main__':
    avengers = Film('avengers - infinity war', 2018, 160)
    avengers.give_like()
    avengers.give_like()
    avengers.give_like()
    avengers.give_like()
    avengers.give_like()
    avengers.give_like()
    avengers.give_like()
    print('Name: ' + avengers.name + ' Year: ' + str(avengers.year) + ' Duration: ' + str(avengers.duration) + " Likes"
                                                                                                               ": " +
          str(avengers.likes))

    atlanta = Series('atlanta', 2018, 2)
    atlanta.give_like()
    atlanta.give_like()
    atlanta.give_like()
    print('Name: ' + atlanta.name + ' Year: ' + str(atlanta.year) + ' Season: ' + str(atlanta.season) + " Likes: " + str(atlanta.likes))
