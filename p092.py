# A number chain is created by continuously adding the square of the digits in
#  a number to form a new number until it has been seen before.
# How many starting numbers below ten million will arrive at 89?

def arrivesAt89(n):
	if n == 89:
		return True
	elif n == 1:
		return False
	else:
		return arrivesAt89(nextChain(n))

def nextChain(n):
	numsList, total = [], 0
	while n > 0:
		numsList.append(n % 10)
		n //= 10
	while len(numsList) > 0:
		temp = numsList.pop()
		total += temp ** 2
	return total


print(len([i for i in range(1, 10000001) if arrivesAt89(i)]))

# 8581146