#!/usr/bin/env python3
user_input = input('please enter text ')
lc = user_input.lower().split()
counter = dict((i, lc.count(i)) for i in lc)
for key, value in counter.items():
    if value > 1:
        print(value, '-', key)