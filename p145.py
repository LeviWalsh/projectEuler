# Some positive integers n have the property that the sum [n + reverse(n)]
# consists entirely of odd (decimal) digits.
# How many reversible numbers are there below one-billion?

# takes a string and reverses it
def reverse(s):
	if len(s) == 1:
		return s
	else:
		return s[-1] + reverse(s[:-1])

def allOdds(s):
	if len(s) == 1 and int(s) % 2 == 1:
		return True
	elif int(s[0]) % 2 == 1:
		return allOdds(s[1:])
	else:
		return False

numReversible = []
for i in range(1, 1000000001):
	if i % 10 != 0 and allOdds(str(i + int(reverse(str(i))))):
		numReversible.append(i)
		
print(len(numReversible))

# 608720