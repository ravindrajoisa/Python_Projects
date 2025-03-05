import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', ':', ';', '<', '>']

no_letters = int(input("How many letters do you want in your password: "))
no_numbers = int(input("How many numbers do you want in your password: "))
no_symbols = int(input("How many symbols do you want in your password: "))

password_list = []

for i in range(0, no_letters):
    char = random.choice(letters)
    password_list += char

for i in range(0, no_numbers):
    char = random.choice(numbers)
    password_list += char
    
for i in range(0, no_symbols):
    char = random.choice(symbols)
    password_list += char

print("Before Shuffle: ", password_list)
random.shuffle(password_list)
print("After Shuffle: ", password_list)
password=""

for char in password_list:
    password += char

print("Here is the password: ", password)