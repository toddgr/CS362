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

import unittest

def leapYear(year):
    print('The year is: ', year)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('YES', year, 'is a leap year\n')
                return True
            else:
                print('NO', year, 'is NOT a leap year\n')
                return False
        else:
            print('YES', year, 'is a leap year\n')
            return True
    else:
        print('NO', year, 'is NOT a leap year\n')
        return False


class Testing(unittest.TestCase):
    
    # Assert that the function correctly calculates the given year to be a leap year.
    def test1(self):
        self.assertEqual(leapYear(2020), True)
        self.assertEqual(leapYear(1840), True)
        self.assertEqual(leapYear(1696), True)
        self.assertEqual(leapYear(1708), True)

    # Assert that the function coorectly calculates the given year to NOT be a leap year.
    def test2(self):
        self.assertEqual(leapYear(1789), False)
        self.assertEqual(leapYear(1967), False)
        self.assertEqual(leapYear(1673), False)
        self.assertEqual(leapYear(1781), False)

if __name__ == '__main__':
    unittest.main()