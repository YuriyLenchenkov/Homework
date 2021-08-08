#!/usr/bin/env python3
# Minimum missed number function
def min_num (o):
    sort = sorted(o)
    k = 0
    for i in sort:
        if (sort[k] in sort) and ((sort[k] + 1) not in sort):
            break
        else:
            print('missed number is ', min_num(int(inp)))
            k += 1
    return sort[k] + 1
# input numbers from user
inp = input('Please enter space-delimited non-negative integer numbers: ').split(' ')
# Exceptions catching
# catching negative numbers
for i in inp:
    if int(i) < 0:
        print('negative number exists, please enter again')
        exit()
# catching duplicates
d = {}
for i in inp:
    d.update({i: inp.count(i)})
if len(d) < len(inp):
    print('duplicate values, please enter again')
    exit()
# catching no holes
inp_s = sorted(inp)
delta = (int(inp_s[1])) - (int(inp_s[0]))
t_min = int(min(inp_s))
t_max = int(max(inp_s))
range_list = list(range(t_min, t_max+1, delta))
if (''.join(str(inp).replace("'",''))) == (''.join(str(range_list))):
    print('no holes')
    exit()
print('missed number is ', min_num(inp))