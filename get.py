from connection import create_connection

def get_connection():
    return create_connection()

def select_all_category_names():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT name FROM category')
    return cursor.fetchall()

def select_all_from_category():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM category')
    return cursor.fetchall()

def select_category_by_id(id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM category WHERE id = {id}')
    return cursor.fetchone()

def select_once_by_cid_and_date(id, date):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM once WHERE categoryId = {id} AND dateOf = '{date}'")
    return cursor.fetchall()

def select_time_by_date_endtime_cid(id, date):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM time WHERE categoryId = {id} AND end IS NULL AND dateOf = '{date}'")
    return cursor.fetchall()

# def select_time_by_start_end(id, date, week):
#     connection = get_connection()
#     cursor = connection.cursor()
#     cursor.execute = cursor.execute