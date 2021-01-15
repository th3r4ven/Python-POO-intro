
class Date:

    def __init__(self, day, month, year):
        self.__day = str(day)
        self.__month = str(month)
        self.__year = str(year)

    def formated(self):
        print(self.__day + "/" + self.__month + "/" + self.__year)