#!/usr/bin/env python3
# Minimum missed number function
def min_num(o):
    sort = sorted(o)
#    print(sorted(o))
    k = 0
    for i in sort:
        if (sort[k] in sort) and ((sort[k] + 1) in sort):
            k += 1
#    print(sort[k], sort[k] + 1, k)
#
        else:
#            print('missed number is ', min_num(inp))
#            k += 1
            return sort[k] + 1
# input numbers from user
inp = (input('Please enter space-delimited non-negative integer numbers: ')).split(' ')
inp_int = list(map(int, inp))
# print(inp_int)
# Exceptions catching
# catching negative numbers
for i in inp:
    if int(i) < 0:
        print('negative number exists, please enter again')
        exit()
# catching duplicates
#d = {}
#for i in inp:
#    d.update({i: inp.count(i)})
#if len(d) < len(inp):
#    print('duplicate values, please enter again')
#    exit()
# catching no holes
#t_min = min(inp_int)
#t_max = max(inp_int)+1
#range_list = list(range(t_min, t_max))
#if (sum(inp_int) == sum(range_list)):
#    print('no holes, enter again ')
#    exit()
#printing missed number after checks
print('missed number is ', min_num(inp_int))

