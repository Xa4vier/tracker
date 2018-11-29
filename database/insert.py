from database.connection import create_connection

def get_connection():
    return create_connection()

# account

def insert_user(name, password):
    params = (name, password)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO User (name, password) VALUES(%s, %s)', params)
    connection.commit()
    connection.close()

# category

def insert_category(name, time, money, once, pot, points, userId):
    params = (name, time, money, once, pot, int(points), userId)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Category (name, time, money, once, pot, points, userId) VALUES(%s, %s, %s, %s, %s, %s, %s)', params)
    id = cursor.lastrowid
    connection.commit()
    connection.close()
    return id

# Once

def insert_once(categoryId, date):
    params = (categoryId, date)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Once (categoryId, dateOf) VALUES(%s, %s)', params)
    connection.commit()
    connection.close() 

# money

def insert_money(categoryId, money, date):
    params = (categoryId, money, date)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)
    connection.commit()
    connection.close()  

# time

def insert_time_start(categoryId, dateOf, start):
    params = (categoryId, dateOf, start)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Time (categoryId, dateOf, start) VALUES(%s, %s, %s)', params)
    connection.commit()
    connection.close() 

# pot

def insert_pot(categoryId, amount, dateOf, startDate, endDate):
    params = (categoryId, amount, dateOf, startDate, endDate)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Pot (categoryId, amount, dateOf, startDate, endDate) VALUES(%s, %s, %s, %s, %s)', params)
    connection.commit()
    connection.close() 

def insert_transaction(potId, userId, amount, dateOf):
    params = (potId, userId, amount, dateOf)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Transaction (potId, userId, amount, dateOf) VALUES(%s, %s, %s, %s)', params)
    connection.commit()
    connection.close() 