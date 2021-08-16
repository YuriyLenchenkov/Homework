#!/usr/bin/env python3
inp = input('plese enter value to convese to celsius or fahrenheit (example:25c or 77f) ')
numbers = int(inp[:-1])
if inp[-1].lower() == 'f':
    c = int((lambda numbers: (numbers-32)/1.8)(numbers))
    if c <= -273:
        print('ooops, reached absolute zero')
    else:
        print(f'conversion to celcius is {c}')
if inp[-1].lower() == 'c':
    f = int((lambda numbers: (numbers*1.8 + 32))(numbers))
    if f <= (-459):
        print('ooops, reached absolute zero')
    else:
        print(f'conversion to fahrenheit is {f}')
