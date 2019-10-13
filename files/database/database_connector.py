import mysql.connector
import traceback
from mysql.connector import Error
from .db_utils import DUPLICATE_ENTRY
from files.credentials import database_ip, database_name, database_user, database_password

def get_connection():
    global cursor
    global db
    global sql_error
    
    try:
        db = mysql.connector.connect(
            host = database_ip,
            database = database_name,
            user = database_user,
            password = database_password
        )
        print('\n')
        print('Connected to MySQL Server')
        
        cursor = db.cursor()
    except Error as e:
        print('Error while connecting to MySQL', e)

sql_error = None
db = None
cursor = None
        
def close_connection():
    if db != None and db.is_connected():
        cursor.close()
        db.close()
        print('Disconnected from MySQL Server')

def insert(table_name: str, fields: list, values: list):
    result = -1
    
    fields_formatted = ', '.join(fields).join(('(', ')'))
    values_formatted = '('
    for i in range(0, len(values)):
        if i > 0:
            values_formatted = values_formatted + ', '
        
        if (values[i].type == 'text'):
            values_formatted = values_formatted + '\'%s\''%values[i].value
        else:
            values_formatted = values_formatted + '%s'%values[i].value
        
    values_formatted = values_formatted + ')'
    command = 'INSERT INTO %s %s VALUES %s'%(table_name, fields_formatted, values_formatted)
    
    try:
        get_connection()
        
        if cursor != None and db.is_connected():
            cursor.execute(command)
            result = cursor.lastrowid
            db.commit()
            print("Created object with id: %d"%result)
    except Error as e:
        print('Unable to execute command:\n    %s'%command)
        print('Details:\n    %s'%e)
        
        formatted_exc = traceback.format_exc()
        if 'Duplicate entry' in traceback.format_exc() and 'UNIQUE' in formatted_exc:
            result = DUPLICATE_ENTRY
    finally:
        close_connection()
        
    return result

def delete(table_name: str, conditions: list, values: list):
    rows_deleted = 0
    
    command = 'DELETE FROM %s WHERE %s='%(table_name, conditions[0])
    if values[0].type == 'text':
        command = command + '\'%s\''%values[0].value
    else:
        command = command + '%s'%values[0].value
    
    if len(conditions) > 1:
        for i in range(1, len(conditions)):
            command = command + ' and %s='%conditions[i]
            
            if values[i].type == 'text':
                command = command + '\'%s\''%values[i].value
            else:
                command = command + '%s'%values[i].value

    try:
        get_connection()
        
        if cursor != None and db.is_connected():
            cursor.execute(command)
            rows_deleted = cursor.rowcount
            db.commit()
            print("Rows deleted:\n    %d"%rows_deleted)
    except Error as e:
        print('Unable to execute command:\n    %s'%command)
        print('Details:\n    %s'%e)
    finally:
        close_connection()
        
    return rows_deleted

def fetch(table_name: str, single: bool, conditions: list, values: list):
    result = None
    
    command = 'SELECT * FROM %s WHERE %s='%(table_name, conditions[0])
    if values[0].type == 'text':
        command = command + '\'%s\''%values[0].value
    else:
        command = command + '%s'%values[0].value
    
    if len(conditions) > 1:
        for i in range(1, len(conditions)):
            command = command + ' and %s='%conditions[i]
            
            if values[i].type == 'text':
                command = command + '\'%s\''%values[i].value
            else:
                command = command + '%s'%values[i].value

    try:
        get_connection()
        
        if cursor != None and db.is_connected():
            cursor.execute(command)
            
            if single:
                result = cursor.fetchone()
            else:
                result = cursor.fetchall()
    except Error as e:
        print('Unable to execute command:\n    %s'%command)
        print('Details:\n    %s'%e)
    finally:
        close_connection()
        
    return result

def select(table_name: str, conditions, values) -> list:
    return fetch(table_name, False, conditions, values)

def select_one(table_name: str, conditions, values) -> list:
    return fetch(table_name, True, conditions, values)