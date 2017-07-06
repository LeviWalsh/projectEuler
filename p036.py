# Find the sum of all numbers, less than one million, which are palindromic 
# in base 10 and base 2.

# takes in a string and checks if it is a palindrome
def isPalindrome(s):
	if len(s) <= 1:
		return True
	else:
		# recursively calls isPalindrome if the first and last digit match
		if s[0] == s[-1]:
			return isPalindrome(s[1:-1])
		else:
			return False

# removes the 0b and calls isPalindrome
def binPalindrome(n):
	binaryNum = bin(n)[2:]
	return isPalindrome(binaryNum)

print(sum([i for i in range(1, 1000000) if binPalindrome(i) and isPalindrome(str(i))]))