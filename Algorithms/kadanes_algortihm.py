a = list(map(int, input("Enter the array elements: ").split()))

max_sum = a[0]
current_sum = a[0]

for i in range(1, len(a)):
    current_sum = max(a[i], current_sum + a[i])
    max_sum = max(max_sum, current_sum)

print("Maximum sum =", max_sum)