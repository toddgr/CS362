# Grace Todd
# CS 362: Software Engineering II
# Spring 2021

# Write tests for a simple calculator app. Your app should take two numbers as inputs (a,b). 
# Should have the following methods: addition, subtraction, multiplication, division. 
# Create a test module that has your test cases. 

#import for unit testing
import unittest

# Class with calculator methods
class Calculator:

	def addition(self, a, b):
		sum = a + b
		return sum

	def subtraction(self, a, b):
		dif = a - b
		return dif

	def multiplication(self, a, b):
		prod = a * b
		return prod

	def division(self, a, b):
		if b == 0: 
			print('ERROR: divisor cannot be zero')
		else:
			quot = a // b
			return quot

class Test(unittest.TestCase):
	calc = Calculator()

	def test_addition(self):
		self.assertEqual(self.calc.addition(1, 1), 2)
		self.assertEqual(self.calc.addition(0, 0), 0)
		self.assertEqual(self.calc.addition(200, 100), 300)

	def test_subtraction(self):
		self.assertEqual(self.calc.subtraction(1, 1), 0)
		self.assertEqual(self.calc.subtraction(5, 2), 3)
		self.assertEqual(self.calc.subtraction(3, 0), 3)

	def test_multiplication(self):
		self.assertEqual(self.calc.multiplication(1 ,1), 1)
		self.assertEqual(self.calc.multiplication(1234, 0), 0)
		self.assertEqual(self.calc.multiplication(0, 40), 0)

	def test_division(self):
		self.assertEqual(self.calc.division(1, 1), 1)
		self.assertEqual(self.calc.division(4, 2), 2)
		self.assertEqual(self.calc.division(60, 30), 2)

if __name__ == '__main__':
	unittest.main()
