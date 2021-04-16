class Budget():
    def __init__(self, category):
        self.category = category
        self.balance = 0.0

    def withdraw(self, amount):
        try:
            amount = float(amount)
        except ValueError as e:
            print(e)
            return None
        if self.balance < amount:
            print(f"The balance is too low to withdraw {amount}, you have a balance of {self.balance}")
        else:
            self.balance -= amount
            print(f"{amount} has been withdrawn.")
    
    
    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError as e:
            print(e)
            return None
        self.balance += amount
        print(f"{amount} has been deposited.")
    
    
    def transfer_balance(self, budget_cat):
        budget_cat.balance += self.balance
        self.balance = 0
        print(f" You have transfered the balance for budget of {budget_cat.category} to {self.category}")

