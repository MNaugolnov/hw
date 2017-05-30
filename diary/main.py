import zadachi as z

def obrabotchik():
    print('Вас приветствует Дневник учета скважин! Что будем делать?')
    print('1 - Вывести список скважин')
    print('2 - Добавить скважину')
    print('3 - Отредактировать параметры скважин')
    print('4 - Присвоить скважине статус Пробурена')
    print('5 - Присвоить скважине статус Не пробурена')
    print('6 - Выйти')

    dey = 1

    while int(dey) != 6: #если не "Выход"
        
        conn = z.initialize(z.connect())
        
        
        dey = int(input('Введите номер действия '))
        if dey == 1:
            z.zadacha1()
        elif dey == 2:
            z.zadacha2(conn, input('Введите полное имя скважины '))
        elif dey == 3:
            z.zadacha3()
        elif dey == 4:
            z.zadacha4()
        elif dey == 5:
            z.zadacha5()
        elif dey == 6:
            z.zadacha6()
            break
        else:
            print('Такого действия нет. Введите число от 1 до 6')

obrabotchik()
        
