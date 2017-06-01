import sys

import zadachi as z

get_conn = lambda: z.connect('wellbase.sqlite')

def act_vyvod_vseh():
    with get_conn() as conn:
        wells = z.z_vyvod_vseh(conn)

    for well in wells:
        print('{well[field_name]} - {well[long_well_name]} - {well[drilled]}'.format(well=well))


def act_add_well():
    ok = False

    while not ok:
        long_well_name = input('\nВведите имя скв.: ')

        if not long_well_name:
            break

        if long_well_name:
            with get_conn() as conn:
                long_well_name = z.z_add_new(conn, long_well_name)
 
            ok = True

def act_update_well():
    pass

def act_drilled_well():
    pass

def act_undrilled_well():
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

def act_quit():
    """Обработчик действия Выйти"""
    sys.exit(0)

       

def main():
    with get_conn() as conn:
        z.initialize(conn)

    act_show_menu()

    actions = {
        '1': act_vyvod_vseh,
        '2': act_add_well,
        '3': act_update_well,
        '4': act_drilled_well,
        '5': act_drilled_well,
        'm': act_show_menu,
        'q': act_quit
    }    

   # print(actions)
    
    while 1:  #while True
        cmd = input('\nВведите номер действия: ')
        action = actions.get(cmd)

        if action:
            action()
        else:
            print('Такая команда неизвестна!')
