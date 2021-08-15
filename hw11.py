#!/usr/bin/env python3

def list_letters(first, last, step=1):
    a = "abcdefghijklmnopqrstuvwxyz"
    first_index = list(a).index(first)
    last_index = list(a).index(last)
    l = []
    if int(step) > 0:
        position = first_index
        while position <= last_index:
            l.append(a[position])
            position = (position + int(step))
        return l
    elif int(step) < 0:
        position = first_index
        while position >= last_index:
            l.append(a[position])
            position = (position - abs(int(step)))
        return l

inp = input('please enter space separated first letter, last letter and step ')
try: #if step exists
    if inp[4] == '-':
        first = inp[0]
        last = inp[2]
        step = inp[4]+inp[5]
        print(list_letters(first, last, step))
    else:
        first = inp[0]
        last = inp[2]
        step = inp[4]
    print(list_letters(first, last, step))
except IndexError:
    first = inp[0]
    last = inp[2]
    print(list_letters(first, last))
