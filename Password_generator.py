import random
import string

len = int(input("Enter length of password(6 to 15) : "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(len):
    password += random.choice(characters)

print("\n----PASSWORD GENERATED SUCCESSFULLY----")
print("\nGenerated Password: ",password)