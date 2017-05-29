import zadachi as z

def obrabotchik():
    print('Вас приветствует ваш Ежедневник! Что будем делать?')
    print('1 - Вывести список задач')
    print('2 - Добавить задачу')
    print('3 - Отредактировать задачу')
    print('4 - Завершить задачу')
    print('5 - Начать задачу сначала')
    print('6 - Выйти')

    dey = 1

    while int(dey) != 6: #если не "Выход"

        dey = int(input('Введите номер действия '))
        if dey == 1:
            z.zadacha1()
        elif dey == 2:
            z.zadacha2()
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
        
