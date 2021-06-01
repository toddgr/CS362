# Grace Todd
# CS 362: Software Engineering II
# Spring 2021

# Program 2, unittest testing, and pytest testing
# Ask the user for a sentence and determine the number of words in that sentence.
# Write tests for the above specification using unittest and pytest. 
# Document the outputs in a PDF - screenshots of the output from unittest and pytest

# test_program2.py

import pytest
import Program2

def test_wordCount():
    assert Program2.wordCount('testing testing testing') == 3
    assert Program2.wordCount('first second third fourth fifth sixth') == 6

def test_wordNumCount():
    assert Program2.wordCount('testing 1 testing 2 testing 3 testing 4 test') == 9
    assert Program2.wordCount('Rule number 1 about fight club is we dont talk about fight club') == 13