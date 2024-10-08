class MinimumBalanceError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class BankAccount:
    __name: str
    __account_number: str
    __balance: float

    def __init__(self, name: str, account_number: str, balance: float):
        self.__name = name
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount: float):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance - amount < 1000:
            raise MinimumBalanceError("Minimum balance must be 1000")

        if self.__balance < amount:
            print("You don't have sufficient balance")
            return
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


acc1 = BankAccount("john", "123456", 1000)

print(acc1.get_balance())

acc1.deposit(100)
acc1.deposit(100)

try:
    acc1.withdraw(100)
    acc1.withdraw(100)
    acc1.withdraw(100)
except MinimumBalanceError as e:
    raise e

print(acc1.get_balance())
