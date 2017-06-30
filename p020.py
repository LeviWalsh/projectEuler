# Find the sum of the digits in the number 100!

def factorial(n):
	assert n >= 0, "Factorial numbers can't be negative"
	assert n % 1 == 0, "Factorial must be done on integers"

	if n == 0 or n == 1:
		return 1
	else:
		return n * factorial(n-1)

# Stolen from p016 
def sum_digits(n):
	total = 0
	while n > 0:
		total += (n % 10)
		n = n // 10
	return total

print(sum_digits(factorial(100)))

# 648