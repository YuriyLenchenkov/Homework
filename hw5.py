#!/usr/bin/env python3

# Minimum missed number function
def min_num (o):
    sort = sorted(o)
    k = 0
    for i in sort:
        if (sort[k] in sort) and ((sort[k] + 1) not in sort):
            break
        else:
            print('missed number is ', min_num(inp_num))
            k += 1
    return sort[k] + 1
# input numbers from user
inp = input('Please enter space-delimited non-negative integer numbers: ').split(' ')

# Exceptions catching
# catching negative number
try:
    inp_num = [*map(int, inp)]
    for i in inp_num:
        if i < 0:
            print('negative number exists, please enter again')
            exit()

    print('missed number is ', min_num(inp_num))
except:
    print('Please correct your mistakes')