def get_transaction_summary(transactions):
    total_credits = 0
    total_debits = 0
    transaction_count = 0

    for transaction in transactions:
        transaction_type = transaction[0]
        amount = transaction[1]

        if transaction_type == "credit":
            total_credits += amount
            transaction_count += 1
        elif transaction_type == "debit":
            total_debits += amount
            transaction_count += 1

    net_balance = total_credits - total_debits

    summary = [
        {"total_credits": total_credits},
        {"total_debits": total_debits},
        {"net_balance": net_balance},
        {"transaction_count": transaction_count}
    ]

    return summary
sample_transactions = [
    ["credit", 2000],
    ["debit", 500],
    ["credit", 300]
]
summary_output = get_transaction_summary(sample_transactions)
print(summary_output)