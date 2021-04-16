# Grace Todd
# CS 262
# Divisor app

# Write a program that lists all the possible divisors for given number

# Retrieve user input, typecast variable as integer
num = input("Select a number: ")
num = int(num)

divisors = []

for i in range(1, int(num / 2) + 1):
    if num % i == 0:
        divisors.append(i)

print("Divisors of ", num, "are: ", divisors)