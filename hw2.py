#!/usr/bin/env python3

import time

input = input("Please input any text, numbers, symbols and spaces you want: ").split(' ')
start = time.time()
lst = list(input)
for i in lst:
    while lst.count(i) > 1:
        lst.remove(i)
result1 = " "
print(result1.join(lst),'\n')
end = time.time()
print ('Elapsed time with loop\n', end - start, '\n')

start = time.time()
result2 = list(dict.fromkeys(lst))
result2_str = " "
print(result2_str.join(result2),'\n')
end = time.time()
print ('Elapsed time with dict function\n', end - start)