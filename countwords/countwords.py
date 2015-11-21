#!/usr/bin/python3

""" Word Counter 

Counts the number of individual words in a string. 
For added complexity read these strings in from a text file and generate a summary.

Taken from https://github.com/karan/Projects 

Author: toashel @ http://github.com/toashel 

"""

import sys, string

word_dict = {}

def report():
	print("Word Count Report: \n")

	for key in sorted(word_dict, key = word_dict.get, reverse = True):
		print("Occurrences of {0}: {1}".format(key, str(word_dict[key])))

def word_count(word):
	if word not in word_dict:
		word_dict[word] = 1
	else:
		word_dict[word] += 1

def main():
	filename = sys.argv[-1]
	file = open(filename, 'r')
	text = file.read().split()
	words = [word.strip(string.punctuation) for word in text]
	file.close()

	for word in words:
		word_count(word)

	report()

if __name__ == "__main__":
	main()


