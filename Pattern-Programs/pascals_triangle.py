# Pascal's Triangle

rows = int(input("Enter number of rows:"))

for i in range(rows):
    num = 1

    # Print spaces
    for j in range(rows - i - 1):
        print(" ", end=" ")

    # Print numbers
    for j in range(i + 1):
        print(num, end="   ")
        num = num * (i - j) // (j + 1)

    print()