n = int(input("Enter a number: "))

prime = True

if n <= 1:
    prime = False

for i in range(2, n):
    if n % i == 0:
        prime = False

if prime:
    print("Prime Number")
else:
    print("Not a Prime Number")