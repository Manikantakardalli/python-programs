# Electricity Bill Generator

customer_name = input("Enter Customer Name: ")
customer_id = input("Enter Customer ID: ")
units = int(input("Enter Units Consumed: "))

if units <= 100:
    bill = units * 2

elif units <= 200:
    bill = (100 * 2) + (units - 100) * 3

elif units <= 300:
    bill = (100 * 2) + (100 * 3) + (units - 200) * 5

else:
    bill = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

tax = bill * 0.05
total = bill + tax

print("\n========== ELECTRICITY BILL ==========")
print("Customer Name :", customer_name)
print("Customer ID   :", customer_id)
print("Units Used    :", units)
print("Bill Amount   : ₹", bill)
print("Tax (5%)      : ₹", tax)
print("Total Amount  : ₹", total)

   

 