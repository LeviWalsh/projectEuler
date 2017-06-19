# What is the 10 001st prime number?

def isPrime(n):
	assert n > 1: "Primes are always greater than 1"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [2]
n = 3
while len(primes) < 10001:
	if isPrime(n):
		primes.append(n)
	n += 2

print(primes[-1])

# 104743