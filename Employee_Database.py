employee = {}

n = int(input("Enter no.of employees: "))

for i in range(n):
    name = input(f"Enter Name of employee {i+1}: ")
    salary = int(input("Enter Salary: "))
    employee[name] = salary

highest = max(employee, key=employee.get)

print("Employee Database:", employee)
print("Highest Salary:", employee[highest])
print("Employee with Highest Salary:", highest)
