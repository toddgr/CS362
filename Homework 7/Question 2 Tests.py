# Grace Todd
# CS 362: Software Engineering II
# Spring 2021

# Homework 7
# Question 2: From homework 1, rewrite the leap year program using the test-first approach.
# Years that are evenly divisible by 4 except years that are evenly divisible by 100 unless
# the years are also evenly divisible by 400 

# Testing file

import unittest
import Q2Code

class TestCase(unittest.TestCase):

    # First test asserts that years that ARE evenly divisible by 4 are counted as a leap year by the function.
    def test1(self):
        self.assertEqual(Q2Code.leapYear(1888), 'Yes')
        self.assertEqual(Q2Code.leapYear(1828), 'Yes')
        self.assertEqual(Q2Code.leapYear(2000), 'Yes')
        self.assertEqual(Q2Code.leapYear(1944), 'Yes')

if __name__ == '__main__':
    unittest.main()