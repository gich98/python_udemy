import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

password = ""

length_password = num_letters + num_symbols + num_numbers

while len(password) < length_password:
    random_choice = random.randint(0, 2)
    if random_choice == 0 and num_letters != 0:
        password += random.choice(letters)
        num_letters -= 1
    elif random_choice == 1 and num_symbols != 0:
        password += random.choice(symbols)
        num_symbols -= 1
    elif random_choice == 2 and num_numbers != 0:
        password += random.choice(numbers)
        num_numbers -= 1

print(f"The password generated is: {password}. It's length is {len(password)}")
