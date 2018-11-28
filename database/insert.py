from database.connection import create_connection

def get_connection():
    return create_connection()

def insert_category(name, time, money, once, points):
    params = (name, time, money, once, int(points))
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO category (name, time, money, once, points) VALUES(%s, %s, %s, %s, %s)', params)
    connection.commit()
    connection.close()

# Once

def insert_once(categoryId, date):
    params = (categoryId, date)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO once (categoryId, dateOf) VALUES(%s, %s)', params)
    connection.commit()
    connection.close() 

# money

def insert_money(categoryId, money, date):
    params = (categoryId, money, date)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)
    connection.commit()
    connection.close()  

# time

def insert_time_start(categoryId, dateOf, start):
    params = (categoryId, dateOf, start)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO time (categoryId, dateOf, start) VALUES(%s, %s, %s)', params)
    connection.commit()
    connection.close() 