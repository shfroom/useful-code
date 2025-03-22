#!/usr/bin/env python3

import math

def is_prime(n):
	for x in range(2, math.floor(math.sqrt(n)) + 1):
		if n % x == 0:
			return False
	return True

print(is_prime(10))
print(is_prime(11))