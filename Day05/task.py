import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# random_letters = random.choices(letters, k = nr_letters)
#
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# random_symbols = random.choices(symbols, k = nr_symbols)
#
# nr_numbers = int(input(f"How many numbers would you like?\n"))
# random_numbers = random.choices(numbers, k = nr_numbers)
#
# easy_version = random_letters + random_symbols + random_numbers
# hard_version = random.sample(easy_version, len(easy_version))
#
# print("Your password is: " + "".join(hard_version))

#Easy version
print("Welcome to the PyPassword Generator!")
password = ""
nr_letters = int(input("How many letters would you like in your password?\n"))
for letter in range(0, nr_letters):
    password += random.choice(letters)

nr_symbols = int(input(f"How many symbols would you like?\n"))
for symbol in range(0, nr_symbols):
    password += random.choice(symbols)

nr_numbers = int(input(f"How many numbers would you like?\n"))
for number in range(0, nr_numbers):
    password += random.choice(numbers)

print(password)

#Hard version
print("Welcome to the PyPassword Generator!")
password_list = []
nr_letters = int(input("How many letters would you like in your password?\n"))
for letter in range(0, nr_letters):
    password_list.append(random.choice(letters)) #can do .append or the += (both produce same result)

nr_symbols = int(input(f"How many symbols would you like?\n"))
for symbol in range(0, nr_symbols):
    password_list += random.choice(symbols)

nr_numbers = int(input(f"How many numbers would you like?\n"))
for number in range(0, nr_numbers):
    password_list += random.choice(numbers)

random.shuffle(password_list)
password = ""
for character in password_list:
    password += character
print("Your password is: " + password)

