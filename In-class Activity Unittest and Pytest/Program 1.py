# Grace Todd
# CS 362: Software Engineering II
# Spring 2021

# Program 1, unittest testing, and pytest testing
# This first program will store and return usernames using set and get functions.

# import unittesting class, pytest class
import unittest
import pytest

class User:
	user = []

	# Store usernames
	def set_user(self, username):
		self.user.append(username)
		return len(self.user) - 1

	# Return username
	def get_user(self, userID):
		if userID >= len(self.user):
			return 'ERROR: Username does not exist'
		else:
			return self.user[userID]

# UNITTEST CLASS FOR THE USER CLASS
class Testing(unittest.TestCase):
	user = User()
	userID = []
	username = []

	# Test case function to check the set_user function
	def test_set_user(self):
		print('SET USER TEST\n')

		for i in range(5): # Test 5 cases of usernames
			user_name = 'User ' + str(i)
			self.username.append(user_name)
			userID = self.user.set_user(user_name)

			self.assertIsNotNone(userID) # Assert that userID is stored
			self.userID.append(userID) # Store userID into userID list

			# Print userID list
			print("userID length = ", len(self.userID))
			print(self.userID)

			# Print usernames list
			print('user_name length = ', len(self.username))
			print(self.username)

			print('\nFINISH SET USER TEST')

	# Test case function to check the get_user function
	def test_get_user(self):
		print('\nSTART GET USER TEST\n')

		length = len(self.userID) # Store total number of stored username information
		print('userID length = ', length)
		print('username length = ', len(self.username))

		for i in range(6):
			if i < length: #If I does not exceed the total length, then verify the username that has been returned
				self.assertEqual(self.username[i], self.user.get_user(self.userID[i])) # If the two names do not match, then the test case will fail
			else:
				print('Testing for GET_USER no user test')
				self.assertEqual('ERROR: Username does not exist', self.user.get_user(i)) # If the length exceeds, check for error message
				print('\nFinish GET_USER test\n')

if __name__ == '__main__':
	unittest.main()
	