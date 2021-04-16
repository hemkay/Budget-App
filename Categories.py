from BudgetClass import Budget

entertainment = Budget('Entertainment')
food = Budget('Food')
clothing = Budget('Clothing')
entertainment.deposit('20w')
print(entertainment.balance)