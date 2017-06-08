def fibonachi(s):
    i = 1
    f1 = 0
    f2 = 1
    while i <= s:
        fn = f1 + f2
        f1, f2 = f2, fn
        i +=1
        yield f1
        
s = int(input('Введите количество элементов ряда '))

fib = [ x for x in fibonachi(s)]
print(fib) #список

st = ' '.join([str(i) for i in fib])
print(st) #строкой как в условиях дз
