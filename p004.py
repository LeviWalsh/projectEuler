# Find the largest palindrome made from the product of two 3-digit numbers.

def reverse(num):
	string = str(num)
	if string == '':
		return
	else:
		first = string[0]
		return int(str(reverse(string[1:])) + str(first))

largest = 0
for i in range(100, 1000):
	for j in range(100, 1000):
		if i * j == reverse(i * j) and i * j > largest:
			largest = i * j
print(largest)

# 906609