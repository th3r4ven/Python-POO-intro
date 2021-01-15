

class Account:

    def __init__(self, number, owner, balance, limit):
        print('Creating object... {}'.format(self))
        self.number = number  # Class Attribute
        self.owner = owner
        self.balance = balance
        self.limit = limit

    def create(self):
        pass


if __name__ == '__main__':
    account = Account(666, "Raven", 10000000, 999999)

    # Accessing class attribute
    print(account.balance)
