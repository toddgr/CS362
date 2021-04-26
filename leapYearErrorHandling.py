# Grace Todd
# CS 262
# Leap year calculator WITH ERROR HANDLING
# Program takes in user input, tests input for integer data type, and requests new input until input is integer.
print("Is it a leap year? Let's find out!")

#ERROR HANDLING
while True:
    try:
        # Year variable is given by user input.
        yearInput = input("Enter a year: ")
        year = int(yearInput)
    except:
        print("ERROR: input must be a number. Please try again.")
        continue
    else:
        break

print("Year: ", year) # Clarifies what year is being calculated in the output window

# Leap year calculations
print("Calculating . . . ")
if (year % 4) == 0: # Checks if year is divisible by four. If yes, Check if year is divisible by 100

    if (year % 100) == 0: # Checks if year is divisible by 100. If yes, check if year is divisible by 400.

        if (year % 400) == 0: #Checks if year is evenly divisible by 400. If yes, year IS a leap year.
            print(year, " is a leap year.")
        else: # If year is not divisible by 400:
            print(year, " is NOT a leap year.")
    else: # If year is not evenly divisible by 100:
            print(year, " is a leap year.")

else: # If year is not evently divisible by four:
    print(year, " is NOT a leap year.")