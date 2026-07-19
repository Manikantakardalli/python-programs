# Restaurant Billing System

customer_name = input("Enter Customer Name: ")

print("\n----------- MENU -----------")
print("Burger      : ₹120")
print("Pizza       : ₹250")
print("Pasta       : ₹180")
print("Cold Drink  : ₹50")
print("----------------------------")

burger = int(input("Enter Burger Quantity: "))
pizza = int(input("Enter Pizza Quantity: "))
pasta = int(input("Enter Pasta Quantity: "))
drink = int(input("Enter Cold Drink Quantity: "))

burger_bill = burger * 120
pizza_bill = pizza * 250
pasta_bill = pasta * 180
drink_bill = drink * 50

subtotal = burger_bill + pizza_bill + pasta_bill + drink_bill

gst = subtotal * 0.05

total = subtotal + gst

print("\n========== RESTAURANT BILL ==========")
print("Customer Name :", customer_name)
print("--------------------------------------")
print("Burger      :", burger, "x 120 =", burger_bill)
print("Pizza       :", pizza, "x 250 =", pizza_bill)
print("Pasta       :", pasta, "x 180 =", pasta_bill)
print("Cold Drink  :", drink, "x 50  =", drink_bill)
print("--------------------------------------")
print("Subtotal    : ₹", subtotal)
print("GST (5%)    : ₹", gst)
print("Total Bill  : ₹", total)
print("--------------------------------------")
print("Thank You! Visit Again 😊")