balance = 10000
pin = 1234

print("========== WELCOME TO ATM ==========")

entered_pin = int(input("Enter Your 4-Digit PIN: "))

if entered_pin != pin:
    print("Incorrect PIN!")
else:
    while True:

        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            print("Available Balance: Rs.", balance)

        elif choice == 2:
            amount = float(input("Enter Deposit Amount: Rs. "))

            if amount > 0:
                balance += amount
                print("\nAmount Deposited Successfully.")
                print("\nCurrent Balance: Rs.", balance)
            else:
                print("Invalid Amount!")

        elif choice == 3:
            amount = float(input("Enter Withdrawal Amount: Rs. "))

            if amount <= 0:
                print("Invalid Amount!")

            elif amount > balance:
                print("Insufficient Balance!")

            else:
                balance -= amount
                print("\nPlease Collect Your Cash.")
                print("\nRemaining Balance: Rs.", balance)

        elif choice == 4:
            old_pin = int(input("Enter Current PIN: "))

            if old_pin == pin:
                new_pin = int(input("Enter New PIN: "))
                confirm_pin = int(input("Confirm New PIN: "))

                if new_pin == confirm_pin:
                    pin = new_pin
                    print("PIN Changed Successfully.")
                else:
                    print("PIN Mismatch!")

            else:
                print("Incorrect Current PIN!")

        elif choice == 5:
            print("\nThank You for Using Our ATM.")
            break

        else:
            print("Invalid Choice! Please Try Again.")