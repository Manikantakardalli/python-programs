def isprime(n):
    if n<2:
        return False
    
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
        

    return True

start = int(input("Enter  Starting number:"))
end = int(input("Enter last number:"))

for n in range(start,end+1):
    if isprime(n):
        print(n)