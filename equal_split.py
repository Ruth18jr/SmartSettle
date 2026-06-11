from ledger import set_balance


def calculate_equal_split(payments, total):
    share = total / len(payments)

    for name, amount_paid in payments.items():
        set_balance(name, amount_paid - share)
