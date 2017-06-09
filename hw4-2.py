import string
import random

symb = string.digits + string.ascii_letters 

def password(s):
    def pwd(s): 
        i = 1
        while i <= s: 
            i +=1
            yield random.choice(symb) 
                
    pasw = ''.join([str(i) for i in pwd(s)])
    return pasw

s = int(input('Введите длину желаемого пароля ')) 
print(password(s)) 
print(password(s)) 
print(password(s)) 
