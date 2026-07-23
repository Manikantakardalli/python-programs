expenses = []

print("Welcome to Expense Tracker")
print("--------------------------------")

while True:

    print("\n========= MENU =========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        amount = float(input("Enter amount: ₹"))
        category = input("Enter category (Food/Travel/Shopping/etc): ")

        expense = {
            "amount": amount,
            "category": category
        }

        expenses.append(expense)

        print("\nExpense Added Successfully!")

    elif choice == "2":

        if len(expenses) == 0:
            print("\nNo expenses found!")

        else:
            print("\n------ Expense List ------")

            for i in range(len(expenses)):
                print(i + 1, ". Category :", expenses[i]['category'])
                print("   Amount   : ₹", expenses[i]['amount'])
                print("---------------------------")

    elif choice == "3":

        if len(expenses) == 0:
            print("\nNo expenses available!")

        else:
            total = 0

            for expense in expenses:
                total += expense["amount"]

            print(f"\n💰 Total Expense = ₹{total}")

            print("\n------ Category Summary ------")

            summary = {}

            for expense in expenses:

                category = expense["category"]

                if category in summary:
                    summary[category] += expense["amount"]
                else:
                    summary[category] = expense["amount"]

            for category in summary:
                print(category, ": ₹", summary[category])

    elif choice == "4":

        print("\n Thank you for using Expense Tracker!")
        break

    else:
        print("\n Invalid Choice! Please try again.")