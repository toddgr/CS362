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

#Type cast input as integer
firstNum = int(firstNum)
secondNum = int(secondNum)

#Error handling for division funnction
while secondNum == 0:
    print("ERROR: Cannot compute division, zero is not valid divisor.")
    secondNum = input("Enter new number: ")
    secondNum = int(secondNum)

else:

    #Addition function
    sum = firstNum + secondNum
    print("ADDITION: ", firstNum, " + ", secondNum, " = ", sum)

    #Subtraction function
    dif = firstNum - secondNum
    print("SUBTRACTION: ", firstNum, " - ", secondNum, " = ", dif)

    #Multiplication function
    prod = firstNum * secondNum
    print("MULTIPLICATION: ", firstNum, " * ", secondNum, " = ", prod)

    #Division function
    quot = firstNum // secondNum
    print("DIVISION: ", firstNum, " / ", secondNum, " = ", quot)