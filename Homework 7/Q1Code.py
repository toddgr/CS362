# Grace Todd
# CS 362: Software Engineering II
# Spring 2021

# Homework 7
# Question 1: Write a program that prints the numbers from 1 to 100. But for multiples of three print 
# "Fizz" instead of the number nad for the multiples of five print "Buzz". For numbers which are 
# multiples of both three and five print "FizzBuzz".

# Code implementation

def fizzbuzz(i):
	if i % 3 == 0:
#		if i % 5 == 0:
#			print('Fizzbuzz')
#			return 'Fizzbuzz'
#		else:
		print('Fizz')
		return 'Fizz'
#	elif i % 5 == 0:
#		print('Buzz')
#		return 'Buzz'
	else:
		print(i)
		return i
