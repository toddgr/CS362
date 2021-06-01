# Grace Todd
# CS 362: Software Engineering II
# Spring 2021

# Homework 7
# Question 2: From homework 1, rewrite the leap year program using the test-first approach. 

# Code implementation

def leapYear(year):
    if year % 4 == 0:
        return 'Yes'
    else:
        return 'No'
