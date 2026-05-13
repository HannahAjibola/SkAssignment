def calculate_balance(transactions):
    balance = 0
    for amount in transactions:
            balance += amount
    return balance

print(calculate_balance([]))