import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
          'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']
print("*****Welcome to the password Generator*****\n-------------------------------------------")
number_of_letters = int(input("How many letters would you like in your password: "))
number_of_symbols = int(input("How many symbols would you like in your password: "))
number_of_numbers = int(input("How many numbers would you like in your password: "))

password = []
for char in range(1, number_of_letters + 1):
    random_char = random.choice(letters)
    password += random_char

for sym in range(1, number_of_symbols + 1):
    random_sym = random.choice(symbols)
    password += random_sym

for num in range(1, number_of_numbers + 1):
    random_num = random.choice(numbers)
    password += random_num

generated_password = random.shuffle(password)

password_str = ""
for char in password:
    password_str += char


print(password_str)