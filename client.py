

class Client:

    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    # Using property to create get and setters

    @property
    def name(self):
        return self.__name.title()

    @name.setter
    def name(self, name):
        self.__name = name


if __name__ == '__main__':
    client = Client("raven", "exemple@exemple.com")
    print(client.get_email())
    client.set_email("raven@exemple.com")

    # Calling get and setters using @property
    # Simple syntax
    print(client.name)
    client.name = "Matheus"
    print(client.name)
