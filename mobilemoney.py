class Mobile_money:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance is {self.balance}."
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance is {self.balance}."
        else:
            return "Insufficient funds or invalid withdrawal amount."

    def check_balance(self):
        return f"Current balance is {self.balance}."
    
myAccount = Mobile_money("Jamey", 1000)
print(myAccount.check_balance())
print(myAccount.deposit(500))
print(myAccount.withdraw(200))
