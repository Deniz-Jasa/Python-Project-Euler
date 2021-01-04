# Python Project Euler - Problem 5 - Deniz Jasarbasic

# Question: 2520 is the smallest number that can be divided by each 
# of the numbers from 1 to 10 without any remainder. What is the 
# smallest positive number that is evenly divisible by all of the 
# numbers from 1 to 20?

# Solution:

import math

def compute():

	result = 1

	for i in range(1, 21):
		result *= i // math.gcd(i, result)

	return str(result)

print(compute())