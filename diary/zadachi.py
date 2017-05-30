"""
Функции дневника по бурению скважин
"""
import sqlite3
import os.path as Path

SQL_SELECT_ALL = '''
    SELECT
        id, field_name, long_well_name, drilled
    FROM
        welldiary
'''

SQL_SELECT_WELL_BY_ID = SQL_SELECT_ALL + ' WHERE id=?'
SQL_SELECT_WELL_BY_LONGNAME = SQL_SELECT_ALL + ' WHERE long_well_name=?'

SQL_INSERT_WELL = '''
    INSERT INTO welldiary(
        long_well_name  
    ) VALUES (
        ?
    )
'''

def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name) #otkrytie soedineniya

    return conn

def initialize(conn):
    with conn:
        script_file_path = Path.join(Path.dirname(__file__), 'sqlbase.sql')
        
        with open(script_file_path) as f:
            conn.executescript(f.read())

def zadacha1():
    print('Эта функция будет выводить список всех скважин со статусом бурения за указанный день. По умолчанию, за текущий день.')

def zadacha2(conn, long_well_name):
    print('Эта функция пытается добавлять новую скважину в указанную дату.')

    if not long_well_name:
        print('Ошибка! Введите полное имя скважины')
        return

    with conn:
        found = find_well_by_longname(conn,  ) 

        if found:
            return found[2]

        cursor = conn.execute(SQL_INSERT_WELL, (long_well_name,))

        # Здесь будет обработчик по добавлению
        return

          
def zadacha3():
    print('Эта функция будет редактировать параметры скважины, используя уникальный идентификатор в БД. Если скважина не найдена, то выводится ошибка.')

def zadacha4():
    print('Эта функция будет менять статус скважины на Пробурена.')
   
def zadacha5():
    print('Эта функция будет менять статус скважины на Не пробурена.')
          
def zadacha6():
    print('Выход.')
    

