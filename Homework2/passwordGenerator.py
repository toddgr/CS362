# Grace Todd
# CS 262
# Password Generator

# Import functions for random generation
import string
import random

# Write a program that takes in a number as input and returns a password of that length.
print("--- P A S S W O R D    G E N E R A T O R ---")

#Prompt user for variable input, typecast variable as integer
len = input("Please enter password length: ")
len = int(len)

#create list from which random numbers and letters can be chosen from
chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
password = [] #create empty list to fill with random generator

#create random list
for i in range(len):
    password.append(random.choice(chars))

#pull password from list
newPassword = ''.join(password)

# Output new password
print(" ")
print(". . . C A L C U L A T I N G . . . ")
print("Congratulations! Here is your new password: ")
print(newPassword)