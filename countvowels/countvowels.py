#!/usr/bin/python3

""" Vowels Counter 

Enter a string and the program counts the number of vowels in the text. 
For added complexity have it report a sum of each vowel found.

Taken from https://github.com/karan/Projects 

Author: toashel @ http://github.com/toashel 

"""

def main(string):
	vowel_dict = {'A':0, 'E':0, 'I':0, 'O':0, 'U':0}
	count = 0

	for letter in string:
		if letter.upper() in vowel_dict:
			vowel_dict[letter.upper()] += 1
			count += 1

	print("Number of vowels:", str(count))
	for vowel in sorted(vowel_dict):
		print(vowel + ": " + str(vowel_dict[vowel]))


if __name__ == "__main__":
	string = input("Please enter a string: \n")
	main(string)




