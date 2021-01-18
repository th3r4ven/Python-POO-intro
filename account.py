from dates import Date


class Account:

    transfer_tax = 10

    def __init__(self, number, owner, balance, limit):
        self.__number = number  # Class Attributes
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit

    def deposit(self, value):
        self.__balance += value
        print("Successful, you deposit " + str(value) + " in your account\n")

    def __can_withdraw(self, value):
        return value <= (self.__balance + self.__limit)

    def withdraw(self, value):
        if self.__can_withdraw(value):
            self.__balance -= value
            print("You withdraw $" + str(value) + "\n")
        else:
            print("Not enough balance\n")

    def statement(self):
        print("Your bank statement is " + str(self.__balance) + "\n")

    def transfer(self, value, acc):
        self.withdraw(value + Account.transfer_tax)
        acc.deposit(value)

    @property
    def balance(self):  # Getter
        return self.__balance

    @property
    def owner(self):
        return self.__owner

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit

    @staticmethod
    def bank_code():
        return "001"

    @staticmethod
    def bank_codes():
        return {"Nubank": '123', "Next": '321', "Inter": "267"}


if __name__ == '__main__':
    account = Account(666, "Raven", 150, 999999)
    account2 = Account(555, 'Owner 2', 15, 90)

    # Accessing class method (class functions)
    account.transfer(15, account2)
    account.statement()

    # Using get and setters
    print(account.limit)
    account.limit = 999
    print(account.limit)

    # Challenge
    d = Date(15, '01', 2021)
    d.formated()
