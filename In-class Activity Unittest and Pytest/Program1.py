# Grace Todd
# CS 362: Software Engineering II
# Spring 2021

# Program 1, unittest testing, and pytest testing
# Ask the user for a string and determine whether it is a palindrome or not. 
# Write tests for the above especification using unittest and pytest.
# Document the outputs in a PDF - screenshots of the output from unittest and putest

# import unittesting class, pytest class
import unittest

# Function that compares the input against the input reversed, returns true or false
def strResult(string):
	return string == string[::-1]

def palindrome(str):
	#Ask the user for a string
	#print('Please enter a string: ')
	#str = input()

	#Reverse the input, store true or false value
	result = strResult(str)
	#Print output result
	print('The string given is: ', str)
	if result:
		print('YES, ', str, ' is a palindrome.\n')
		return True
	else: 
		print('NO, ', str, 'is not a palindrome.\n')
		return False


# UNITTEST CLASS FOR THE PALINDROME CLASS
class Testing(unittest.TestCase):
	
	# Test to assert that function is able to identify palindromes by checking output against True
	def test1(self):
		self.assertEqual(palindrome('tacocat'), True)
		self.assertEqual(palindrome('amoroma'), True)
		self.assertEqual(palindrome('racecar'), True)

	# Test to assert that function is able to identify NON palindromes by checking output against False
	def test2(self):
		self.assertEqual(palindrome('taco cat'), False)
		self.assertEqual(palindrome('dennis'), False)
		self.assertEqual(palindrome('opportunity'), False)

if __name__ == '__main__':
	unittest.main()
	