"""
Функции дневника по бурению скважин
"""
import sqlite3
import os.path as Path

SQL_SELECT_ALL = '''
    SELECT
        id, long_well_name, field_name, drilled
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

SQL_UPDATE_WELL = '''
    UPDATE welldiary(
        long_well_name  
    ) SET (
        ?
    )
'''

SQL_STATUS_WELL = '''
    SELECT CASE (
    drilled
    )
    WHEN "1" THEN "Well is drilled"
    ELSE "Well is not drilled"
    END
    FROM
        welldiary
'''

def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name) #otkrytie soedineniya

    return conn

def initialize(conn):
    with conn:
        script_file_path = Path.join(Path.dirname(__file__), 'sqlitebd.sql')
        
        with open(script_file_path) as f:
            conn.executescript(f.read())

def z_vyvod_vseh(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
        return cursor.fetchall()
    
def z_add_new(conn, long_well_name):
    if not long_well_name:
        # Здесь должна быть ошибка
        return

    with conn:
        found = find_well_by_longname(conn, long_well_name)

        if found:
            return found[2]

        cursor = conn.execute(SQL_INSERT_WELL, (long_well_name,))

        # Здесь магия
        return
          
def z_update():
    print('Эта функция будет редактировать параметры скважины, используя уникальный идентификатор в БД. Если скважина не найдена, то выводится ошибка.')

def z_drilled():
    print('Эта функция будет менять статус скважины на Пробурена.')
   
def z_undrilled():
    print('Эта функция будет менять статус скважины на Не пробурена.')
          
def find_well_by_longname(conn, long_well_name):

    with conn:
        cursor = conn.execute(
            SQL_SELECT_WELL_BY_LONGNAME, (long_well_name,)
        )
        return cursor.fetchone()

