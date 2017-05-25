# By considering the terms in the Fibonacci sequence whose values do not exceed 
# four million, find the sum of the even-valued terms.

def fib(curr, prev, limit):
	summation = 0
	while curr < limit:
		if curr % 2 == 0:
			summation += curr
		curr, prev = prev+curr, curr
	return summation

print(fib(1, 0, 4000000))

# 4613732