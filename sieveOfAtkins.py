# After I did p010 I realized it would be good to invest some time making a better
# algorithm for finiding prime numbers. Clearly didn't do all on my own, check out
# these links:
# https://en.wikipedia.org/wiki/Sieve_of_Atkin
# https://stackoverflow.com/questions/21783160/sieve-of-atkin-implementation-in-python

import math

def quickPrimes(limit):
    Primes = [2,3]
    sieve = [False]*(limit+1)
    for x in range(1, int(math.sqrt(limit))+1):
        for y in range(1, int(math.sqrt(limit))+1):
            n = 4*x**2 + y**2
            if n<=limit and (n%12==1 or n%12==5):
                sieve[n] = not sieve[n]
            n = 3*x**2+y**2
            if n <= limit and n%12 == 7:
                sieve[n] = not sieve[n]
            n = 3*x**2 - y**2
            if x > y and n <= limit and n%12 == 11:
                sieve[n] = not sieve[n]
    for x in range(5, int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x**2, limit+1, x**2):
                sieve[y] = False
    for p in range(5,limit):
        if sieve[p]:
            Primes.append(p)
    return Primes




