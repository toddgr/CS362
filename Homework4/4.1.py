
#Grace Todd
#Cs 362 Software Engineering II
#Spring 2021

#Homework 4
#Question 1: Write code to calculate the volume of a cube, and then use the unittest module and write any 3 tests that can test out your code.

#Import unittest module
import unittest

#Write code to calculate the volume of a cube. 
def calc_cube(side):
    side = int(side)
    if type(side) not in [int]:
        raise TypeError("ERROR: Input must be an integer.")
    else:
        if side < 0:
            raise Exception("ERROR: Input must be a positive integer")
        else:
            volume = side ** 3
            print("Volume of cube with side length ", side, " is: ", volume)
            return volume


#Unit Testing class
class TestCube(unittest.TestCase):

    #Unit Test to assert that the volume is correctly calculated
    def test_vol(self):
        self.assertEqual(calc_cube(4), 64)
        self.assertEqual(calc_cube(21), 9261)
        self.assertEqual(calc_cube(9), 729)
        self.assertEqual(calc_cube(0), 0)

    #Unit Test to determine whether the input value is properly detected, and whther or not an invalid typecast is excepted correctly.
    def test_input(self):
        self.assertRaises(TypeError, calc_cube, True, 2.532)
        self.assertRaises(TypeError, calc_cube, True, 3.14126)
        self.assertRaises(TypeError, calc_cube, True, 'str')

    #Unit Test to determine whether or not the negative integer error is callable.
    def test_sign(self):
        self.assertRaises(Exception, calc_cube, True, -4)
        self.assertRaises(Exception, calc_cube, True, -16.234)
        self.assertRaises(Exception, calc_cube, True, -98.66)


#Call functions for testing user interface
#input = input("Enter your side value: ")
#calc_cube(input)

# Call Unit Tests
if __name__ == '__main__':
    unittest.main()