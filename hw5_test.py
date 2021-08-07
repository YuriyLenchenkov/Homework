#!/usr/bin/env python3
# Minimum missed number function
def min_num (o):
    sort = sorted(o)
    k = 0
    for i in sort:
        if (sort[k] in sort) and ((sort[k] + 1) not in sort):
            break
        else:
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
            inp = input('Please enter space-delimited non-negative integer numbers: ').split(' ')
            inp_num = [*map(int, inp)]
#        else:
    print('missed number is ', min_num(inp_num))
#    break

# catching extra spaces and symbols
except ValueError:
    try:
        print('possibly extra spaces or letters between numbers, please enter again')
        inp = input('Please enter space-delimited non-negative integer numbers: ').split(' ')
        inp_num = [*map(int, inp)]
        for i in inp_num:
            if i < 0:
                print('negative number exists, please enter again')
                inp = input('Please enter space-delimited non-negative integer numbers: ').split(' ')
                inp_num = [*map(int, inp)]
#            else:
        print('missed number is ', min_num(inp_num))
#        break
# user should think twice before entering something
    except:
        print('\n!!!!!!!!!!\nUnexpected error\n!!!!!!!!!!')







