# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

arr, curr, prev = [], 1, 0

def digits(n):
	count = 0
	while n > 0:
		n = n // 10
		count += 1
	return count
	
while True:
	if digits(curr) >= 1000:
		break
	arr.append(curr)
	curr, prev = curr + prev, curr

print(len(arr) + 1)



# 4782
