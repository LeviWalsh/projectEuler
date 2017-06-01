# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

factors = []
def prime_factors(n):
	for i in range(2, n + 1):
		if n % i == 0:
			factors.append(i)
			prime_factors(n // i)
			break
prime_factors(600851475143)
print(max(factors))

# 6857