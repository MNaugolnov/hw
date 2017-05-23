def quater(x, y):

    if x > 0 and y > 0:
        k = ('в I четверти')
    elif x < 0 and y > 0:
        k = ('в II четверти')
    elif x < 0 and y < 0:
        k = ('в III четверти')
    elif x > 0 and y < 0:
        k = ('в IV четверти')
    elif x == 0 and y == 0:
        k = ('в начале координат')
    else:
        k = ('на оси координат')
    return k

x = float(input('Введите координату Х:'))
y = float(input('Введите координату Y:'))
    
print ('Точка лежит {}'.format(quater(x, y)))
