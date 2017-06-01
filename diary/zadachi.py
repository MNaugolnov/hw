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
        long_well_name, field_name, drilled
    ) VALUES (
        ?, ?, ?
    )
'''

SQL_UPDATE_WELL = '''
    UPDATE welldiary
    SET long_well_name=? , field_name=?, drilled=?
    WHERE ID=?
'''

SQL_STATUS_WELLD = '''
    UPDATE welldiary
    SET drilled='Пробурена'
    WHERE ID=?
'''

SQL_STATUS_WELLU = '''
    UPDATE welldiary
    SET drilled='Не пробурена'
    WHERE ID=?
'''


def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name) #otkrytie soedineniya

    return conn

def initialize(conn):
    with conn:
        script_file_path = Path.join(Path.dirname(__file__), 'baza.sql')
        
        with open(script_file_path) as f:
            conn.executescript(f.read())

def z_vyvod_vseh(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
        return cursor.fetchall()
    
def z_add_new(conn, long_well_name, field_name, drilled):

    cursor = conn.execute(SQL_INSERT_WELL, (long_well_name, field_name, drilled))
          
def z_update(conn, long_well_name, field_name, drilled, idu):

    cursor = conn.execute(SQL_UPDATE_WELL, (long_well_name, field_name, drilled, idu))

def z_drilled(conn, idu):
    cursor = conn.execute(SQL_STATUS_WELLD, idu)

def z_undrilled(conn, idu):
    cursor = conn.execute(SQL_STATUS_WELLU, idu)

def find_well_by_longname(conn, long_well_name):

    with conn:
        cursor = conn.execute(
            SQL_SELECT_WELL_BY_LONGNAME, (long_well_name,)
        )
        return cursor.fetchone()
