

class Employeer:

    def __init__(self, name):
        self.name = name

    def register_hour(self, horas):
        print("Registering work hour")

    def show_tasks(self):
        print("Do a lot of things")


class Caelum(Employeer):

    def show_tasks(self):
        print("Do caelum things")

    def search_month_courses(self, month=None):
        print(f'Showing courses - {month}' if month else 'Showing actual month courses')


class Alura(Employeer):

    def show_tasks(self):
        print('Do Alura things')

    def search_unanswered_questions(self):
        print("Searching for unanswered questions")


class Hipster:
    def __str__(self):
        return f'Hipster, {self.name}'


class Junior(Alura):
    pass


class Pleno(Alura, Caelum, Hipster):
    pass


class Senior(Alura, Caelum, Hipster):
    pass


if __name__ == '__main__':
    workerjr = Junior('Raven')
    workerjr.search_unanswered_questions()

    workerpl = Pleno('r4ven')
    workerpl.search_unanswered_questions()
    workerpl.search_month_courses()

    print(workerpl)
