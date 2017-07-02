# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


# returns true if the digits in the number to the fifth power equal the number
def digit_fifth_powers(num):
	digits, forDigits, total = [], num, 0
	while forDigits > 0:
		digits.append(forDigits % 10)
		forDigits //= 10
	while len(digits) > 0:
		total += digits[0] ** 5
		digits = digits[1:]
	return total == num

totalSum = 0
# 354294 is the max becuase 6 * 9^5 which has 6 digits. 7 * 9^5 doesn't have 7 digits.
for i in range(10, 354295):
	if digit_fifth_powers(i):
		totalSum += i
print(totalSum)

# 443839