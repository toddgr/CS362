# Grace Todd
# CS 362: Software Engineering II
# Spring 2021

# In-class activity: unittest, pytest, Coverage, pytest-cov

# Write tests for leap year program before you begin implementation. 
# Make a commit. 
# Write code and then run the test - then make a commit
# Document Output with unittest
# Run pytest and document the output.
# Run coverage - with report option and coverage with report -m. Again document the output. 
# Run coverage with html - document the output. 
# Run pytest cov - document the output

# test_leapYear.py

import pytest
import leapYearTest

def test_leapYear():
    assert leapYearTest.leapYear(1868) == True
    assert leapYearTest.leapYear(1876) == True
    assert leapYearTest.leapYear(1992) == True
    assert leapYearTest.leapYear(1948) == True

def test_nonleapYear():
    assert leapYearTest.leapYear(1881) == False
    assert leapYearTest.leapYear(1941) == False
    assert leapYearTest.leapYear(1989) == False
    assert leapYearTest.leapYear(2021) == False