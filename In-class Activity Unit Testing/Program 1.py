# Grace Todd
# CS 362: Software Engineering II
# Spring 2021

# Program 1, unittest testing, and pytest testing
# This first program will store and return usernames using set and get functions.

# import unittesting class
import unittest

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

# Unittesting class for the User class
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

	def test_boolean(self):
		a = True
		b = True
		self.assertEqual(a, b)

if __name__ == '__main__':
	unittest.main()

	user = User()
	user.set_user('Bojack')
	user.set_user('Todd')
	user.set_user('Diane')
	user.set_user('Carolyn')

	print('Username is stored with ID ', user.set_user('Gracey'))
	print('Username stored with ID 0 is', user.get_user(0))