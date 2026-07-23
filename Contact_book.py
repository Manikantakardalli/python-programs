contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display Contacts")
    print("4. Delete Contact")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        contacts[name] = phone
        print("Contact Added Successfully!")

    elif choice == 2:
        name = input("Enter Name to Search: ")
        if name in contacts:
            print(f"{name} : {contacts[name]}")
        else:
            print("Contact Not Found!")

    elif choice == 3:
        if len(contacts) == 0:
            print("No Contacts Available.")
        else:
            print("\n----- Contact List -----")
            for name, phone in contacts.items():
                print(name, ":", phone)

    elif choice == 4:
        name = input("Enter Name to Delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact Deleted Successfully!")
        else:
            print("Contact Not Found!")

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")