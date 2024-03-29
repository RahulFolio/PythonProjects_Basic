# Program to Create a Password Generator

# import random module
import random

# create variables
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")

# create input variables
nr_letters = int(input("How many letters would you like in your password?: ")) 
nr_symbols = int(input(f"How many symbols would you like?: "))
nr_numbers = int(input(f"How many numbers would you like?: "))

# main code

#create a list
password_list = []

# for letters part of the password
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

# for symbols part of the password
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

# for numbers part of the password
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

# for random placement of the characters in the password
random.shuffle(password_list)

# arranging the passsword in acceptable format
password = ""
for char in password_list:
    password += char

# print the generated password
print(f"Your Password is: {password}")