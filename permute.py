#!/usr/bin/env python3

# nPr = !n / !(n - r)

import math

def calculate_permutations(n, r):
	# Calculate the numerator and denominator of the equation.
	# !n / !(n - r)
	# You can alternatively just find the length of the result returned
	# by the "permute_string" function, but this is the equation.
	numerator = math.factorial(n)
	denominator = math.factorial((n - r))
	result = numerator / denominator
	return result

def permute_string(charset, string, result):
	# Recursively calculate the permutations of the charset and
	# return it as a list.
	if result == False:
		result = []
	if len(charset) > 0:
		for i in range(0, len(charset)):
			newString = string + charset[i]
			newCharset = charset[0:i] + charset[i+1:]
			# Recursively calculate with each new charset and add to the result.
			permute_string(newCharset, newString, result)
	else:
		result.append(string)
	return result
	

# Final calculation.
charset = input("Charset: ")
print("Calculating permutations of {charset}...")
result = calculate_permutations(len(charset), len(charset))
print(f"\nThe amount of permutations in the sequence given is {result}")
print(permute_string(charset, "", []))