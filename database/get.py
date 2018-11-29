from database.connection import create_connection

def get_connection():
    return create_connection()

def select_user_by_name(name):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute = cursor.execute
    cursor.execute(f"SELECT * FROM User WHERE name = '{name}'")
    return cursor.fetchone()

### category ###

def select_all_category_names(userId):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(f'SELECT name FROM Category WHERE userId = {userId}')
    return cursor.fetchall()

def select_all_from_category_by_userId(userId):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM Category WHERE userId = {userId}')
    return cursor.fetchall()

def select_category_by_id(userId, categoryId):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM Category WHERE userId = {userId} AND id = {categoryId}')
    return cursor.fetchone()

### once ###

def select_once_by_cid_and_date(id, date):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Once WHERE categoryId = {id} AND dateOf = '{date}'")
    return cursor.fetchall()

def select_once_by_start_end(categoryId, start, end):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute = cursor.execute
    cursor.execute(f"SELECT * FROM Once WHERE categoryId = {categoryId} AND dateOf >= '{start}' AND dateOf <= '{end}'")
    return cursor.fetchall()

### money ###

def select_money_by_start_end(categoryId, start, end):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Money WHERE categoryId = {categoryId} AND dateOf >= '{start}' AND dateOf <= '{end}'")
    return cursor.fetchall()

### time ###

def select_time_by_date_endtime_cid(id, date):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Time WHERE categoryId = {id} AND end IS NULL AND dateOf = '{date}'")
    return cursor.fetchall()

def select_time_by_start_end(categoryId, start, end):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Time WHERE categoryId = {categoryId} AND dateOf >= '{start}' AND dateOf <= '{end}'")
    return cursor.fetchall()

def select_pot_by_categoryId(categoryId):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM pot WHERE categoryId = {categoryId}")
    return cursor.fetchone() 