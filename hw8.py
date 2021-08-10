#!/usr/bin/env python3
def numcheck(o):
    if o.lower() == 'cancel':
        return 'cancel'
    try:
        int(o)
    except ValueError:
        return 'Не удалось преобразовать введенный текст в число.'
    if (int(o) % 2) == 0:
        return int(o)//2
    elif (int(o) % 2) > 0:
        return int(o)*3+1


inp = input('please enter something ')
print(numcheck(inp))
