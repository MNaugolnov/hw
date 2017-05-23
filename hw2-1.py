def palindrom(str):
    str = input('Введите число или строку:')
    str = str.upper() #чтобы капитализация не влияла на решение
    return str == str[::-1]     #return True if str == str[::-1] else False

print('Палиндром? {}'.format(palindrom(str)))

