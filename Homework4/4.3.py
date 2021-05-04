#Grace Todd
#CS 362: Software Engineering II
#Spring 2021

#Homework 4
#Question 3: Write code that generates a full name when you provide the first and last name as inputs, 
##then use the unittest module and write any 3 tests that can test out your code. 

#import unit testing module
import unittest

#import alphabet to ensure that inputs are only letters
import string

#Function that takes in first and last name and combines them into a full name
def fullName(first, last):
    #Check to make sure that there are no numbers or special characters in first and last name
    if first.isalpha() and last.isalpha():
       fullname = first + ' ' + last
       return fullname
    else:
        raise Exception("ERROR: Full names must have only letters. No numbers or special characters permitted.")

#Unit Testing class
class TestName(unittest.TestCase):

    #Unit Test to assert that the output is a string
    def test_strOutput(self):
        self.assertIsInstance(fullName('Bojack', 'Horseman'), str)
        self.assertIsInstance(fullName('Todd', 'Chavez'), str)
        self.assertIsInstance(fullName('Diane', 'Ngyuen'), str)

    #Unit Test to assert that the inputs are both strings with no numbers or special characters
    def test_alpha(self):
        self.assertRaises(Exception, fullName, True, 'Xae A-12', 'Musk')
        self.assertRaises(Exception, fullName, True, '6ix', '9ine')
        self.assertRaises(Exception, fullName, True, 'Joey', 'Bada$$')

        self.assertRaises(Exception, fullName, False, 'Andrew', 'Scheafer')
        self.assertRaises(Exception, fullName, False, 'Grace', 'Todd')
        self.assertRaises(Exception, fullName, False, 'Olivia', 'Mcmains')

# Call Unit Tests
if __name__ == '__main__':
    unittest.main()