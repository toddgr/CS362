# Grace Todd
# CS 362: Software Engineering II
# Spring 2021

# Program 2, unittest testing, and pytest testing
# Ask the user for a sentence and determine the number of words in that sentence.
# Write tests for the above specification using unittest and pytest. 
# Document the outputs in a PDF - screenshots of the output from unittest and pytest

# Import unittest class
import unittest

# Ask the user for a sentence and determine the number of words in that sentence.
def wordCount(sentence):
    print('Input: ', sentence)

    # Split the string into words, count the length and store into a variable
    word_count = len(sentence.split())

    # Return and print the result
    print('Word count: ', str(word_count), '\n')
    return word_count
    
class Testing(unittest.TestCase):

    # Assert that the function returns the correct word count value with the given strings.
    # Also tests to assert the output value is an integer.
    def test1(self):
        self.assertEqual(wordCount('Testing the word count function'), 5)
        self.assertEqual(wordCount('Ask the user for a sentence and determine the number of words in that sentence'), 15)
        self.assertEqual(wordCount('This is an activity'), 4)
        self.assertEqual(wordCount('Write tests for the above specification using unittest and pytest.'), 10)

if __name__ == '__main__':
    unittest.main()