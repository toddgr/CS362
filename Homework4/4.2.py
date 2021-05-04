
#Grace Todd
#CS 362: Software Engineering II
#Spring 2021

#Homework 4
#Question 2: Write code to calculate the average elements in a list, and then use the unittest module and write 3 tests that can test out your code. 

#import unittest for testing, reduce and lambda functions to calculate list average
import unittest
from functools import reduce

#Program that calculates the average of elements in a list, assuming that all elements in a list are either float or int
def calc_avg(list):
    for i in range(len(list)): 

        if isinstance(list[i], int):
            continue
        else:
            raise TypeError("ERROR: List item ", i, "must be an integer.")

    list[i] = int(list[i])

    if len(list) == 0:
        raise Exception("List is empty.")
        return 0
    else:
        avg = reduce(lambda a, b: a + b, list) / len(list)
        return avg

#Unit Testing Class
class TestAvg(unittest.TestCase):

    #Unit Test that checks for empty lists to ensure that the exception is thrown correctly
    def test_emptylst(self):
        self.assertRaises(Exception, calc_avg, True, [])

        self.assertRaises(Exception, calc_avg, False, [1,2,3,4,5])
        self.assertRaises(Exception, calc_avg, False, [12,48,96,765,65])
        self.assertRaises(Exception, calc_avg, False, [2,65,41,855,345,64,655,5])


    #Unit Test to assert that all elements in list are float or integer.
    def test_type(self):
        self.assertRaises(TypeError, calc_avg, True, [1,2,3,4,5,'six'])
        self.assertRaises(TypeError, calc_avg, True, [1,2,3,4,5,3.456,7.141])
        self.assertRaises(TypeError, calc_avg, True, [1,2,'cat',4,5,'fourteen'])

        self.assertRaises(TypeError, calc_avg, False, [6,5,4,3,2,1])

# Call Unit Tests
if __name__ == '__main__':
    unittest.main()
