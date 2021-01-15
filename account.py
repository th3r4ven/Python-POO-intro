from dates import Date


class Account:

    def __init__(self, number, owner, balance, limit):
        self.__number = number  # Class Attribute
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit

    def deposit(self, value):
        self.__balance += value
        print("Successful, you deposit " + str(value) + " in your account")

    def withdraw(self, value):
        if value <= self.__balance:
            self.__balance -= value
            print("You withdraw $" + str(value))
        else:
            print("Not enough balance")

    def statement(self):
        print("Your bank statement is " + str(self.__balance))

    def transfer(self, value, acc):
        self.withdraw(value)
        acc.deposit(value)


if __name__ == '__main__':
    account = Account(666, "Raven", 15, 999999)
    account2 = Account(555, 'Owner 2', 15, 90)
    # Accessing class method (class functions)
    account.statement()
    account.transfer(15, account2)
    account2.withdraw(10)
    account.deposit(100)
    account.statement()

    # Challenge
    d = Date(15, '01', 2021)
    d.formated()
