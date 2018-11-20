from connection import create_connection

def get_connection():
    return create_connection()

def insert_category(name, time, money, once, points):
    params = (name, time, money, once, int(points))
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO category (name, time, money, once, points) VALUES(%s, %s, %s, %s, %s)', params)
    connection.commit()
    connection.close()

def insert_once(categoryId, date):
    params = (categoryId, date)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO once (categoryId, dateOf) VALUES(%s, %s)', params)
    connection.commit()
    connection.close() 

def insert_money(categoryId, money):
    params = (categoryId, money)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO money (categoryId, amount) VALUES(%s, %s)', params)
    connection.commit()
    connection.close()  

def insert_time_start(categoryId, dateOf, start):
    params = (categoryId, dateOf, start)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO time (categoryId, dateOf, start) VALUES(%s, %s, %s)', params)
    connection.commit()
    connection.close() 