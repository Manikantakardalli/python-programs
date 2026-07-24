rooms = []

while True:
    print("\n========== HOTEL MANAGEMENT SYSTEM ==========")
    print("1. Book Room")
    print("2. View All Bookings")
    print("3. Search Customer")
    print("4. Check Out")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        room_no = input("Enter Room Number: ")
        name = input("Enter Customer Name: ")
        age = input("Enter Age: ")
        phone = input("Enter Phone Number: ")
        days = int(input("Enter Number of Days: "))
        rent = days * 1500

        booking = {
            "Room": room_no,
            "Name": name,
            "Age": age,
            "Phone": phone,
            "Days": days,
            "Rent": rent
        }

        rooms.append(booking)

        print("\nRoom Booked Successfully!")
        print("Total Rent: ₹", rent)

    elif choice == "2":
        if len(rooms) == 0:
            print("\nNo Bookings Found!")
        else:
            print("\n========== BOOKING DETAILS ==========")
            for i in rooms:
                print("-------------------------------")
                print("Room Number :", i["Room"])
                print("Customer    :", i["Name"])
                print("Age         :", i["Age"])
                print("Phone       :", i["Phone"])
                print("Days        :", i["Days"])
                print("Rent        : ₹", i["Rent"])

    elif choice == "3":
        search = input("Enter Customer Name: ")

        found = False

        for i in rooms:
            if i["Name"].lower() == search.lower():
                print("\nCustomer Found")
                print("Room Number :", i["Room"])
                print("Age         :", i["Age"])
                print("Phone       :", i["Phone"])
                print("Days        :", i["Days"])
                print("Rent        : ₹", i["Rent"])
                found = True
                break

        if found == False:
            print("Customer Not Found!")

    elif choice == "4":
        room = input("Enter Room Number to Check Out: ")

        found = False

        for i in rooms:
            if i["Room"] == room:
                print("\nCustomer Checked Out Successfully!")
                print("Final Bill: ₹", i["Rent"])
                rooms.remove(i)
                found = True
                break

        if found == False:
            print("Room Not Found!")

    elif choice == "5":
        print("\nThank You for Using Hotel Management System!")
        break

    else:
        print("Invalid Choice!")