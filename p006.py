# Find the difference between the sum of the squares of the first 
# one hundred natural numbers and the square of the sum.

from operator import *

# returns the sum of squares up to n
def sumOfSquares(n):
	count = 0
	while n > 0:
		count += n ** 2
		n -= 1
	return count


# returns the square of the sum up to n
def squareOfSums(n):
	count = 0
	while n > 0:
		count += n
		n -= 1
	return count ** 2


print(squareOfSums(100) - sumOfSquares(100))

# 25164150