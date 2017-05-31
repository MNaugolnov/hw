import sys

import zadachi as z

get_conn = lambda: storage.connect('wellbase.sqlite')

def act_add():
    pass

def act_find():
    pass

def act_find_all():
    pass

def act_show_menu():
    """Обработчик действия показать меню"""
    print('''
Вас приветствует Дневник учета скважин! Что будем делать?

1. Вывести список скважин
2. Добавить скважину
3. Отредактировать параметры скважин
4. Присвоить скважине статус Пробурена
5. Присвоить скважине статус Не пробурена
m. Показать меню
q. Выйти''')

def action_exit():
    """Обработчик действия Выйти"""
    #conn.close()
    sys.exit(0)


######def obrabotchik():
######    print('Вас приветствует Дневник учета скважин! Что будем делать?')
######    print('1 - Вывести список скважин')
######    print('2 - Добавить скважину')
######    print('3 - Отредактировать параметры скважин')
######    print('4 - Присвоить скважине статус Пробурена')
######    print('5 - Присвоить скважине статус Не пробурена')
######    print('6 - Выйти')
######
######    dey = 1
######
######    while int(dey) != 6: #если не "Выход"
######        
######        conn = z.initialize(z.connect())
######        
######        
######        dey = int(input('Введите номер действия '))
######        if dey == 1:
######            z.zadacha1()
######        elif dey == 2:
######            z.zadacha2(conn, input('Введите полное имя скважины '))
######        elif dey == 3:
######            z.zadacha3()
######        elif dey == 4:
######            z.zadacha4()
######        elif dey == 5:
######            z.zadacha5()
######        elif dey == 6:
######            z.zadacha6()
######            break
######        else:
######            print('Такого действия нет. Введите число от 1 до 6')
######
######obrabotchik()
        

def main():
    with get_connection() as conn:
        storage.initialize(conn)

    action_show_menu()

    actions = {
        '1': action_add,
        '2': action_find,
        '3': action_find_all,
        'm': action_show_menu,
        'q': action_exit
    }    

    print(actions)
    
    while 1:  #while True
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd)

        if action:
            action()
        else:
            print('Неизвестная команда!')
