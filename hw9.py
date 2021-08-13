#!/usr/bin/env python3

# Find the difference between the sum of the squares
# of the first one hundred natural numbers
# and the square of the sum.

print(sum([i**2 for i in list(range(1, 100, 1))]) - (sum([i for i in list(range(1, 100, 1))]))**2)

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# a < b < c
# a2 + b2 = c2

print([(a, b, 1000 - int(a) - int(b)) for a in list(range(0, 1000, 1)) for b in list(range(0, 1000, 1))\
    if (int(a) < int(b) and int(b) < (1000 - int(a) - int(b)) and int(a)**2 + int(b)**2 == ((1000 - int(a) - int(b))**2))])


# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

print(str(sum([a**i for a in list(range(1, 1001, 1)) for i in list(range(1,1001,1))]))[-7:])


# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

print([''.join(str(i) for i in range(1, 1000001, 1))[10**p-1] for p in list(range(0, 7, 1))])
