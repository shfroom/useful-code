#!/usr/bin/env python3

import math

def get_number_sequence():
	while True:
		sequence = input("Enter a number sequence: ")
		if sequence.isdigit():
			return [int(x) for x in sequence]
		else:
			print("Invalid input. Please enter a valid number sequence.")
			
sequence = get_number_sequence()
	
# Quicksort
def quicksort(sequence):
	# Choose the middle of the input array as the pivot point and loop through
	# each number to see if it is bigger or smaller than the pivot, and append
	# to lists accordingly.
	while True:
		sorted_sequence = True
		# Loop through the quicksort function until all numbers in the sequence are sorted
		# correctly.
		for i in range(len(sequence) - 1):
			if sequence[i] > sequence[i + 1]:
				sorted_sequence = False
				pivot = sequence[math.floor(len(sequence) / 2)]
				left = []
				right = []
				middle = []
				# Append numbers to the lists corresponding to their value relative to the
				# pivot.
				for j in range(len(sequence)):
					left.append(sequence[j]) if sequence[j] < pivot else None
					right.append(sequence[j]) if sequence[j] > pivot else None
					middle.append(sequence[j]) if sequence[j] == pivot else None
				sequence = left + middle + right
				break
		if sorted_sequence:
			break
	return sequence

print(quicksort(sequence))