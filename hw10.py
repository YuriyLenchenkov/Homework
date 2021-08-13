#!/usr/bin/env python3

a = int(input('please enter positive integer number '))
i = 0
while a > 1:
    if a%2 == 0:
        a = a/2
        i += 1
        print(int(a))
    elif (a%2) > 0:
        a = (a * 3 + 1)
        i += 1
        print(int(a))
print(i)

