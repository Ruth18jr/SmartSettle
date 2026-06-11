import json
from pathlib import Path


HISTORY_FILE = Path(__file__).with_name("transactions.json")


def load_history():
    if not HISTORY_FILE.exists():
        return []

    with open(HISTORY_FILE, "r") as file:
        return json.load(file)


def save_transaction(transactions):
    transaction_history = load_history()
    transaction_history.append(transactions)

    with open(HISTORY_FILE, "w") as file:
        json.dump(transaction_history, file, indent=4)


def show_history():
    print("\n--------TRANSACTION HISTORY--------")    

    transaction_history = load_history()

    if not transaction_history:
        print("No transactions saved yet.")
        return

    for transaction in transaction_history:
        split_type = transaction["type"]
        place = transaction.get("place", "N/A")
        date = transaction["date"]
        people = transaction["people"]

        total_owed = 0
        total_paid = 0
        total_rating = 0
        rating_count = 0

        for name, data in people.items():
            total_owed += data["owed"]
            total_paid += data["paid"]
            if data.get("rating") is not None:
                total_rating += data["rating"]
                rating_count += 1

        print(f"\nDate: {date} | Type: {split_type} | Place: {place}")
        print(f"People: {', '.join(people.keys())}")
        print(f"Total owed: ${total_owed:.2f}")
        print(f"Total paid: ${total_paid:.2f}")

        if rating_count > 0:
            average_rating = total_rating / rating_count
            print(f"Average rating: {average_rating:.1f}/10")

        for name, data in people.items():
            balance = data["paid"] - data["owed"]
            print(f"\n{name}")
            if data.get("ordered"):
                print(f"Ordered: {', '.join(data['ordered'])}")
            print(f"Owed: ${data['owed']:.2f}")
            print(f"Paid: ${data['paid']:.2f}")
            print(f"Balance: ${balance:.2f}")
            if data.get("rating") is not None:
                print(f"Rating: {data['rating']}/10")
