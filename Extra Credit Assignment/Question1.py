"""
Grace Todd
CS 362: Software Engineering II
Spring 2021

EXTRA CREDIT ASSIGNMENT QUESTION 1
Write a program that reverses a sentence.
Input - ask the user for a sentence: a long string
containing multiple words. Return to the user
the same string,  with the words in backward order.
"""


def reverseSentence(str):
	#Split up the string into sentences, put into a list
	sentence = str.split()
	#Reverse the order of the values in the list, reverse sentence by word
	revSentence = sentence[:: -1]
	#Join reversed words together with spaces, so that the output is a string and not a list
	newSentence = " ".join(revSentence)
	#Print new sentence
	print(newSentence)
