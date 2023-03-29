
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#Vanilla Version 1.0
# characters = nr_letters + nr_symbols + nr_numbers
# password = []
# for i in range(int(nr_letters)):
#     random_letter_index = random.randint(0, len(letters)-1)
#     random_index = random.randint(0, characters)
#     password.insert(random_index ,letters[random_letter_index])
# for i in range(int(nr_symbols)):
#     random_symbol_index = random.randint(0, len(symbols)-1)
#     random_index = random.randint(0, characters)
#     password.insert(random_index ,symbols[random_symbol_index])
# for i in range(int(nr_numbers)):
#     random_number_index = random.randint(0, len(numbers)-1)
#     random_index = random.randint(0, characters)
#     password.insert(random_index ,numbers[random_number_index])

# print("".join(password))

#Version Using Python Methods Version 2.0
password = []
for char in range(1, nr_letters + 1):
    password.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))
for char in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))

random.shuffle(password)
print("".join(password))