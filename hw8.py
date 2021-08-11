#!/usr/bin/env python3
def numcheck(r):
    r = int(r)
    if (r % 2) == 0:
        k = 0
        while k < (r//2):
            numcheck(r/2)
            k += 1
        return k
    elif (r / 2) > 0:
        k = 0
        while k <= (r*3):
            numcheck(r/3)
            k += 1
        return k


o = input('please enter smth ')
if o.lower() == 'cancel':
    print('cancel')
    exit()
else:
    try:
        int(o)
    except ValueError:
        print('Не удалось преобразовать введенный текст в число.')
        exit()
print(numcheck(o))
