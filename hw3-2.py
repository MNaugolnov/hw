"""
Модуль перевода из 10-чной в другие системы счисления и наоборот"""

def v10(x, t):
    """Функция для перевода в десятеричную систему счисления"""
    buk = ['A','B','C','D','E','F']
    cif = ['10','11','12','13','14','15']

    a = str(x)
    y = 0

    for i in range(len(a)):
        if t == 16:
            a = list(a)
            for b in range(6):
                if a[i] == buk[b]:
                    a[i] = cif[b]


        k = len(a) - i - 1
        y += int(a[i]) * (t ** k)
    return y

print(v10('98CDE45', 16))
print(v10('DD', 16))
print(v10(11101000, 2))
print(v10(75013, 8))

def iz10(x, t):
    """Функция для перевода из десятеричной системы счисления"""
    buk = ['A','B','C','D','E','F']
    a = ('')

    while x / t > (t - 1):
        i = x % t
        if t == 16 and i > 9:
            i = buk[i-10]

        a += str(i)
        x = x // t

    i = x % t
 
    if t == 16 and i > 9:
        i = buk[i-10]
            
    a += str(i) + str(x // t)
    a = a[::-1]
    return a

## черновик второго способа    
##    while x >= t:
##        i = x % t
##        if t == 16 and i > 9:
##             i = buk[i-10]
##        a.append(str(i))
##        x //= t
##    a.append(str(x))
##    a = a[::-1]
##    return a

print(iz10(571, 8))
print(iz10(7467, 16))
print(iz10(22, 2))
