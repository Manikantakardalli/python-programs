a = list(map(int, input("Enter the array elements: ").split()))

n = len(a)
max = a[0]

for i in range(n):
    for j in range(i, n):
        s = 0
        for k in range(i, j + 1):
            s += a[k]

        if s > max:
            max= s

print("Maximum sum =", max)