a = list(map(int, input("Enter the array elements: ").split()))

n = len(a) + 1

for i in range(1, n + 1):
    if i not in a:
        print("Missing number =", i)
        break