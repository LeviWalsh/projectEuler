# Find the sum of all numbers, less than one million, which are palindromic 
# in base 10 and base 2.

def isPalindrome(n):
	if n < 0:
		return isPalindrome(-n)
	if n < 10:
		return True
	else:
		# recursively calls isPalindrome if the first and last digit match
		if n % 10 == n // (10 * (len(str(n)) - 1)):
			n //= 10
			return isPalindrome(n % (10 * len(str(n)) - 1))
		else:
			return False

def binPalindrome(n):
	# remov
	binaryNum = int(bin(n)[2:])
	return isPalindrome(binaryNum)

print(sum([i for i in range(1, 1000000) if binPalindrome(i) and isPalindrome(i)]))