class BankAccount():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    # Метод для получения текущего баланса счета
    def get_balance(self):
        return self.__balance

    # Метод для внесения денежных средств на счет
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Сумма для внесения должна быть положительной.")

    # Метод для снятия денежных средств со счета
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма для снятия должна быть положительной.")
        if amount > self.__balance:
            raise ValueError("Недостаточно средств на счете.")
        self.__balance -= amount


# Класс для сберегательного счета
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        # Метод super нужен для коректного наследования от родительского класса BankAccount
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    #Функция начисления процентов на остаток по счету
    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)


# Класс для снятия средств без ограничений по балансу
class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)

    def withdraw(self, amount):
        new = self.get_balance() - amount  # Не проверяет, достаточно ли средств
        return new





savings_account = SavingsAccount("Андрей Лонгинов")

savings_account.deposit(500)
print(f"Баланс после депозита: {savings_account.get_balance()}")

#savings_account.withdraw(-100)
#print(f"Баланс после снятия: {savings_account.get_balance()}")

checking_account = CheckingAccount("Андрей Лонгинов", savings_account.get_balance()) # переносим баланс из savings в checking

print(f"Баланс после снятия: {checking_account.withdraw(6000)}")

savings_account.apply_interest()
print(f"Баланс после начисления процентов: {savings_account.get_balance()}")

