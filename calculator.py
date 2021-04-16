# Grace Todd
# CS 262
# Calculator program
# Write a simple calculator app that adds, subtracts, multiplies, and divides



# Introduction
print("--- C A L C U L A T O R     A P P L I C A T I O N ---")

# Create variables that are added together, subtracted from eachother, multiplied and divided
# Request user input

firstNum = input("Enter first number: ")
secondNum = input("Enter second number: ")

#Error handling for division funnction
while secondNum = 0:
    print("ERROR: Cannot compute division, zero is not valid divisor.")
    secondNum = input("Enter new number: ")


#Addition function
sum = firstNum + secondNum
print(firstNum, " + ", secondNum, " = ", sum)

#Subtraction function
dif = firstNum - secondNum
print(firstNum, " - ", secondNum, " = ", dif)

#Multiplication function
