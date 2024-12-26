# Task 2: Password Generator

import random
import string

def password_generator():
    length = int(input("Enter the desired password length: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print("Generated Password:", password)

password_generator()
