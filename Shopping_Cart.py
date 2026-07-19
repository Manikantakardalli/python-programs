cart = {}
bill = 0

n = int(input("Enter number of items: "))

for i in range(n):
    name = input("Enter item name: ")
    price = int(input("Enter price: "))
    qty = int(input("Enter quantity: "))

    total = price * qty
    cart[name] = {
        "Price": price,
        "Quantity": qty,
        "Total": total
    }

    bill += total

print("\n------ BILL ------")
for item, details in cart.items():
    print(item, ":", details)


print("Total Bill =", bill)