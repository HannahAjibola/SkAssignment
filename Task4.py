def apply_interest(balance, rate, years):
    if rate <= 0 or years < 1:
        raise ValueError('Rate must be positive')

    compound_interest = balance * (1 + rate)**years
    return round(compound_interest, 2)