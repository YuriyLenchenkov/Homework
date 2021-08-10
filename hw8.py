#!/usr/bin/env python3
def numcheck(o):
    if o.lower() == 'cancel':
        print('cancel')
        exit()
    else:
        try:
            int(o)
        except ValueError:
            print('Не удалось преобразовать введенный текст в число.')
            exit()
    if (int(o) % 2) == 0:
        print(int(o)//2)
    elif (int(o) % 2) > 0:
        print(int(o)*3+1)


numcheck(input('please enter something '))
