a = list(map(int, input("Enter first sorted list: ").split()))
b = list(map(int, input("Enter second sorted list: ").split()))

merged = a + b
merged.sort()

print("Merged Sorted List:", merged)