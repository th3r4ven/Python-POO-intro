from dates import Date


class Account:

    def __init__(self, number, owner, balance, limit):
        self.number = number  # Class Attribute
        self.owner = owner
        self.balance = balance
        self.limit = limit

    def deposit(self, value):
        self.balance += value
        print("Successful, you deposit " + str(value) + " in your account")

    def withdraw(self, value):
        if value <= self.balance:
            self.balance -= value
            print("You withdraw $" + str(value))
        else:
            print("Not enough balance")

    def statement(self):
        print("Your bank statement is " + str(self.balance))


if __name__ == '__main__':
    account = Account(666, "Raven", 15, 999999)

    # Accessing class attribute
    print("Accessing attribute directly: " + str(account.balance))

    # Accessing class method (class functions)
    account.statement()

    account.withdraw(10)
    account.deposit(100)
    account.statement()

    # Challenge
    d = Date(15, '01', 2021)
    d.formated()
