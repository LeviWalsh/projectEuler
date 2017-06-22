# Find the sum of all the primes below two million.

def isPrime(n):
	assert n > 1: "Primes are always greater than 1"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = []

for i in range(2, 2000000):
	if isPrime(i):
		primes.append(i)

print(sum(primes))

# 142913828922