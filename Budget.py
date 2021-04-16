class Budget():
    def __init__(self, category):
        self.category = category
        self.balance = 0

    def withdraw(self, int: amount):
        if self.balance < amount:
            print(f"The balance is too low to withdraw {amount}, you have a balance of {self.balance}")
        else:
            self.balance -= amount
            print(f"{amount} has been withdrawn.")
    def deposit(self, int: amount):
        self.balance += amount
        print(f"{amount} has been deposited.")
    def transfer_balance(self, Budget: budget_cat):
        budget_cat.balance += self.balance
        self.balance = 0
        print(f" You have transfered the balance for budget of {budget_cat.category} to {self.category}")

entertainment = Budget('entertainment')
food = Budget('food')
food.deposit()
food.transfer_balance(entertainment)
print(entertainment.balance, entertainment.category)
print(food.balance, food.category)