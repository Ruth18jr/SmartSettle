balances = {}


def clear_balances():
    balances.clear()


def add_user(name):
    if name not in balances:
        balances[name] = 0


def set_balance(name, amount):
    balances[name] = amount


def show_balances():
    print("\n---Balances---")

    if not balances:
        print("No balances yet.")
        return

    all_settled = True

    for name, value in balances.items():
        if value > 0:
            print(f"{name} is owed ${value:.2f}")
            all_settled = False
        elif value < 0:
            print(f"{name} owes ${abs(value):.2f}")
            all_settled = False
        else:
            print(f"{name} is settled")

    if all_settled:
        print("Everyone is settled, no payment needed!")
