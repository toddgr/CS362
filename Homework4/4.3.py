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
    if first.isdigit() and last.isdigit():
       raise Exception("ERROR: Full names must have only letters. No numbers permitted.")
       
    else:
        #Initialize all letters in both names to lower case. Capitalize both names. 
        first = first.lower()
        first = first.capitalize()

        last = last.lower()
        last = last.capitalize()

        fullname = first + ' ' + last
        return fullname


#Unit Testing class
class TestName(unittest.TestCase):

    #Unit Test to assert that the output is a string
    def test_strOutput(self):
        self.assertIsInstance(fullName('Bojack', 'Horseman'), str)
        self.assertIsInstance(fullName('Todd', 'Chavez'), str)
        self.assertIsInstance(fullName('Diane', 'Ngyuen'), str)

    #Unit Test to assert that the inputs are both strings with no numbers. dashes and apostrophes allowed.
    def test_alpha(self):
        self.assertRaises(Exception, fullName, True, 'Xae A-12', 'Musk')
        self.assertRaises(Exception, fullName, True, '6ix', '9ine')
        self.assertRaises(Exception, fullName, True, 'Joey', 'Bada$$')

        self.assertRaises(Exception, fullName, False, "Auli'i", 'Cravalho')
        self.assertRaises(Exception, fullName, False, 'Mary', 'Kate-Olsen')
        self.assertRaises(Exception, fullName, False, 'Lily-Rose', 'Depp')

    #Unit test to assert that the first letter of the first namea and last name are capitalized
    def test_capitalized(self):
        self.assertMultiLineEqual(fullName('grace', 'todd'), 'Grace Todd')
        self.assertMultiLineEqual(fullName('PInkY', 'penGUIn'), 'Pinky Penguin')
        self.assertMultiLineEqual(fullName('SARAH', 'LYNN'), 'Sarah Lynn')

# Call Unit Tests
if __name__ == '__main__':
    unittest.main()