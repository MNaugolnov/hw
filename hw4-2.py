import string
import random

symb = string.digits + string.ascii_letters

def pwd(s):

    i = 1

    while i <= s:
        pasi = random.choice(symb)
        i +=1
        yield pasi

    
s = int(input('Введите длину желаемого пароля '))

pasw = ''.join([str(i) for i in pwd(s)])

print(pasw)
