# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?
from operator import mul
from functools import reduce

factors = []
def prime_factors(n):
	for i in range(2, n + 1):
		if n % i == 0:
			factors.append(i)
			prime_factors(n // i)
			break

for i in range(1, 20):
	prime_factors(i)

def mul_list(list):
	reduce(mul, list)

# Get rid of duplicates and then put them back into a list
unique = set(factors)
unique_list = list(unique)

