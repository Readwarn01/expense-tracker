print ("Welcome to my first attempt on building anything with python")
print ("My Expense Tracker")
expenses = []
name = input("Enter your name: ")
breakdown = {}

while True:
    print (f"welcome {name}, what do you want to do?")
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")
    choice = int(input("Choose an option: "))

    if choice == 1:
        category = input("Enter your expense type. E.g food: ")
        amount = float(input("Enter amount: "))
        expenses.append({"category": category, "amount": amount})
        print("Expense added successfully!\n")

    elif choice == 2:
        print(f"{name}, this is breakdown of your expenses")
        for expense in expenses:
            category = expense["category"]
            amount = expense["amount"]

            print(f"{category}: {amount}")

    elif choice == 3:
        print("Breakdown:")
        total = 0
        for expense in expenses:
            category = expense["category"]
            amount = expense["amount"]

            print(f"{category}: {amount}")
            total += amount

        print(f"Total spent: {total}")

    elif choice == 4:
        print("Exiting...")
        print("Done!, Thank you for using My Expense Tracker")

        # print("Breakdown:")
        # for category, amount in breakdown.items():
        #
        #     print(f"{category}: {amount}")
