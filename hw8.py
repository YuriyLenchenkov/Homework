#!/usr/bin/env python3
def numcheck(o):
    if o.lower() == 'cancel':
        return 'cancel'
    try:
        int(o)
    except ValueError:
        return 'Не удалось преобразовать введенный текст в число.'
    r = int(o)
    if (r % 2) == 0:
        return r//2
    elif (r % 2) > 0:
        return r*3+1


inp = input('please enter something ')
print(numcheck(inp))
