#!/usr/bin/env python3

# raw_input() from python2 got renamed and inherited as input() function in python3.
# input() from python2 is deprecated and it can be simulated as eval(input()) in python3
#
# PEP 3105 -- Make print a function https://www.python.org/dev/peps/pep-3105/
# print statement in python2 was replaced by print() function in python3


try:
    from tabulate import tabulate
except:
    print ('You don`t have tabulate module installed :(')
else:
    py_types = [['||||', 'bool', 'str', 'int'], \
            ['bool', '||||', 'true\nor false', '0 or 1'], \
            ['str', 'true\nor false', '||||', 'numbers'], \
           ['int', '0 or 1', 'numbers', '||||']]
    print(tabulate(py_types, headers='firstrow', tablefmt='grid'))
