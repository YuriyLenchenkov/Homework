#!/usr/bin/env python3

import re
inp = input('Please enter numbers, separated with any symbol to calculate sum of numbers ')
num_filter = re.findall("-?[0-9]\d*", inp)
new_list = []
for i in num_filter:
    new_list.append(int(i))
print(sum(new_list))

