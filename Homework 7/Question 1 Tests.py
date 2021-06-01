# Grace Todd
# CS 362: Software Engineering II
# Spring 2021

# Homework 7
# Question 1: Write a program that prints the numbers from 1 to 100. But for multiples of three print 
# "Fizz" instead of the number nad for the multiples of five print "Buzz". For numbers which are 
# multiples of both three and five print "FizzBuzz".

# Testing file

import unittest
import Q1Code

class TestCase(unittest.TestCase):

    # First test asserts that the first four multiples of three are equal to "Fizz"
    def test1(self):
        for i in [3, 6, 9, 12]:
            self.assertEqual(Q1Code.fizzbuzz(i), "Fizz")

    # Second test asserts that multiples of five (that are not also multiples of three) are equal to "Buzz"
    def test2(self):
        for i in [5, 10, 20, 25]:
            self.assertEqual(Q1Code.fizzbuzz(i), "Buzz")

if __name__ == "__main__":
    unittest.main()