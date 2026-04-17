def add_expense(expenses, amount, category):
    expenses.append({"amount": amount, "category": category})

def total_expense(expenses):
    return sum(item["amount"] for item in expenses)

def show_expenses(expenses):
    for item in expenses:
        print(f'{item["category"]}: {item["amount"]}')

def main():
    expenses = []

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            add_expense(expenses, amount, category)

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "3":
            print("Total:", total_expense(expenses))

        elif choice == "4":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
