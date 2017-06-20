# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
from math import *

def pythagoreanTriples(maxSide):
	for a in range(1, maxSide):	
		for b in range(a, maxSide):
			for c in range(b, maxSide):
				if (((a ** 2) + (b ** 2)) == c ** 2) and a + b + c == 1000:
					print([a, b, c])
					return

print(mul(pythagoreanTriples(500))

# [200, 375, 425]
# 31875000