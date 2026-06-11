from ledger import set_balance


def calculate_usage_split(payments):
    for name, data in payments.items():
        owed = data["owed"]
        paid = data["paid"]
        set_balance(name, paid - owed)
