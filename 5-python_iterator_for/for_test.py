import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


sum_data = nr_letters + nr_numbers + nr_numbers
password_data = []


for number in range(0, nr_letters + 1) :
    var_letter = random.randint(0, len(letters)-1)
    print(var_letter)
    password_data+=letters[var_letter]

for number in range(0, nr_numbers+1) : 
    var_numbers = random.randint(0, len(numbers)-1)
    print(var_numbers)
    password_data+=numbers[var_numbers]

for number in range(0, nr_symbols+1) : 
    var_symbols = random.randint(0, len(symbols)-1)
    print(var_symbols)
    password_data +=symbols[var_symbols]

print(password_data)

random.shuffle(password_data)

print(password_data)

password = ''
for char in password_data :
    password+=char

print(password)