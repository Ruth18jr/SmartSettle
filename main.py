from equal_split import calculate_equal_split
from history import save_transaction, show_history
from ledger import add_user, clear_balances, show_balances
from optimizer import optimize_settlement
from usage_split import calculate_usage_split


def get_ordered_items(name):
    ordered = []

    num_meals = int(input(f"How many meals did {name} order? "))
    for meal_num in range(num_meals):
        meal = input(f"Meal {meal_num + 1}: ").strip()
        ordered.append(meal)

    num_drinks = int(input(f"How many drinks did {name} order? "))
    for drink_num in range(num_drinks):
        drink = input(f"Drink {drink_num + 1}: ").strip()
        ordered.append(drink)

    return ordered


def run_equal_split():
    print("\n--------SMARTSETTLE EQUAL SPLIT--------\n")
    clear_balances()

    place = input("Restaurant name: ")
    date = input("Date: ")
    num_people = int(input("Enter the total number of people: "))
    total = float(input("Total amount: $"))

    payments = {}
    transaction = {
        "type": "Equal Split",
        "place": place,
        "date": date,
        "people": {}
    }
    share = total / num_people

    for i in range(num_people):
        name = input(f"Enter name {i + 1}: ").strip()
        ordered = get_ordered_items(name)
        amount_paid = float(input(f"How much did {name} pay? $"))
        rating = float(input("Rating 1-10: "))
        add_user(name)
        payments[name] = amount_paid
        transaction["people"][name] = {
            "ordered": ordered,
            "owed": share,
            "paid": amount_paid,
            "rating": rating
        }

    calculate_equal_split(payments, total)
    show_balances()
    optimize_settlement()
    save_transaction(transaction)


def run_usage_split():
    print("\n--------SMARTSETTLE USAGE BASED--------\n")
    clear_balances()

    transaction = {}
    transaction["type"] = "Usage-Based Split"
    transaction["place"] = input("Restaurant name: ")
    transaction["date"] = input("Date: ")
    transaction["people"] = {}

    num_people = int(input("Enter number of people: "))

    for i in range(num_people):
        name = input(f"Enter name {i + 1}: ").strip()
        ordered = get_ordered_items(name)

        owed = float(input(f"Amount {name} owes: $"))
        paid = float(input(f"Amount {name} paid: $"))
        rating = float(input("Rating 1-10: "))

        add_user(name)
        transaction["people"][name] = {
            "ordered": ordered,
            "owed": owed,
            "paid": paid,
            "rating": rating
        }

    payments = {}
    for name, data in transaction["people"].items():
        payments[name] = {
            "owed": data["owed"],
            "paid": data["paid"]
        }

    calculate_usage_split(payments)
    show_balances()
    optimize_settlement()
    save_transaction(transaction)


def main():
    while True:
        print("\n--------SMARTSETTLE--------")
        print("1. Equal split")
        print("2. Usage-based split")
        print("3. Show history")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            run_equal_split()
        elif choice == "2":
            run_usage_split()
        elif choice == "3":
            show_history()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
