import time

s = int(input('Введите длительность паузы в секундах '))
n = int(input('Факториал какого числа интересует? '))

def paus(s):
    def paus1(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            time.sleep(s)
            print('Пауза длилась {} секунд'.format(s))
            return result
        return wrapper
    return paus1
    

@paus(s)
def factorial(n):
    f = 1

    for i in range(1, n+1):
        f *=i

    return f

print('Факториал {} равен {}'.format(n, factorial(n)))

