#!/usr/bin/env python3
i10 = 0
pal10 = []
#pal2 = []
while i10 <= 10**6:
    i2 = format(i10, "b")
    if (str(i10) == str(i10)[::-1]) and ((i2) == (i2)[::-1]):
        pal10.append(i10)
#        pal2.append(i2)
    i10 += 1
#print(pal10)
#print(pal2)
print('base10 palindrome sum', sum(pal10))
print('base2 palindrome sum', str(bin(sum(pal10, 2))).replace("0b", ''))