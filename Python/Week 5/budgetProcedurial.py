funds = 2500

budgets = {}

expenses = {}

def AddBudget(name, amount):
    global funds
    if name is budgets:
        raise ValueError("Budget for item already exists")
    if amount > funds:
        raise ValueError("Insuffiencent Funds")
    budgets[name] = amount
    funds -= amount
    expenses[name] = 0
    return funds

def Spend(name, amount):
    if name not in expenses:
        raise ValueError("Item not in budget")
    expenses[name] += amount
    budgeted = budgets[name]
    spent = expenses[name]
    return budgeted - spent

def PrintBudget():
    for name in budgets:
        budgeted = budgets[name]
        spent = expenses[name]
        remainingBudget = budgeted - spent
        print(f'{name:15s}, {budgeted:10.2f}, {spent:10.2f} '
              f'{remainingBudget:10.2f}')

print("Total Funds: ", funds)
AddBudget("Books", 100)
AddBudget("Rent", 800)
AddBudget("Car Note", 200)

Spend("Books", 50)
Spend("Rent", 800)
AddBudget("Car Note", 200)

PrintBudget()

