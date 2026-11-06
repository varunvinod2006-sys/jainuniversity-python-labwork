#Bank Transaction Simulation

balance = 0
transactions = []

while True:
    print("\n--- ACCOUNT MENU ---")
    print("1. Deposit")
    print("2. Withdrawal")
    print("3. Balance Inquiry")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            print("Invalid amount!")
        else:
            balance += amount
            transactions.append(("Deposit", amount, balance))
            print("Amount deposited successfully!")

    elif choice == '2':
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount!")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            transactions.append(("Withdrawal", amount, balance))
            print("Amount withdrawn successfully!")

    elif choice == '3':
        print("Current Balance:", balance)

    elif choice == '4':
        print("\n--- TRANSACTION HISTORY ---")
        if len(transactions) == 0:
            print("No transactions yet.")
        else:
            for t in transactions:
                print(t)

    elif choice == '5':
        print("Thank you!")
        break

    else:
        print("Invalid choice! Try again.")
