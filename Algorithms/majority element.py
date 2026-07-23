arr = list(map(int, input("Enter array elements: ").split()))
max = 0
n = None
for num in arr:
       a = arr.count(num)
       if a > max:
             max = a
             n = num
            
if max > len(arr)/2:
      print("Majority Element is", n)
else:
      print("No majority element")
