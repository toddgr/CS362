# Grace Todd
# CS 362: Software Engineering II
# Spring 2021

# Program 1, unittest testing, and pytest testing
# Ask the user for a string and determine whether it is a palindrome or not. 
# Write tests for the above especification using unittest and pytest.
# Document the outputs in a PDF - screenshots of the output from unittest and pytest

# test_program1.py

import pytest
import Program1

def test_palindrome():
    assert Program1.palindrome('asdfgfdsa') == True
    assert Program1.palindrome('oiuytyuio') == True

def test_num_palindrome():
    assert Program1.palindrome('12345654321') == True
    assert Program1.palindrome('123s u s321') == True

def test_palindromeFail():
    assert Program1.palindrome('not a palindrome') == False
    assert Program1.palindrome('this isnt a palindrome either 12323') == False
    assert Program1.palindrome('testing program') == False