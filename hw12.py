#!/usr/bin/env python3
def fib(inp):
    if inp == 1:
        return o[inp]
    elif inp == 0:
        print('you should start from 1 element')
        exit()
    else:
        counter = 2
        while counter < inp:
            o.append(o[counter-1] + o[counter-2])
            counter += 1
        return o[inp-1]


o = [1, 1]
inp = int(input('please enter number '))
print(f'{inp} element of fibonacci is ', fib(inp))
