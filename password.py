import random
import string

length = int(input("Enter the length of the password: "))

if length <= 0:
    print("Password length should be greater than zero.")
else:
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choices(characters, k=length))
    
    print("Password:", password)
