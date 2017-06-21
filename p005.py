# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?

i = 1
for k in (range(1, 21)):
    if i % k > 0:
        for j in range(1, 21):
            if (i*j) % k == 0:
                i *= j
                break
print(i)


# 232792560

# This is not really a coding problem, I arrived at the answer with simple arithmatic
# 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19