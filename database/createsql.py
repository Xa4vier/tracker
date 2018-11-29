from connection import create_connection
from datetime import *

# Get a cursor object
connection = create_connection()
cursor = connection.cursor()

### user and groups ###

cursor.execute('''
    CREATE TABLE User(id INT AUTO_INCREMENT PRIMARY KEY, 
    name TEXT, password TEXT)
    ''')

cursor.execute('''
    CREATE TABLE UserGroup(id INT AUTO_INCREMENT PRIMARY KEY, 
    userId INT, groupId INT)
    ''')

cursor.execute('''
    CREATE TABLE UserGroups(id INT AUTO_INCREMENT PRIMARY KEY, 
    name TEXT)
    ''')
cursor.execute('''
    CREATE TABLE Admin(id INT AUTO_INCREMENT PRIMARY KEY, 
    groupId INT, userId INT)
    ''')

### categories ###

cursor.execute('''
    CREATE TABLE Category(id INT AUTO_INCREMENT PRIMARY KEY, userId INT, name TEXT, groupId INT,
                       time BOOLEAN, money BOOLEAN, once BOOLEAN, pot BOOLEAN, points INT)
                       ''')

cursor.execute('''
    CREATE TABLE Time(id INT AUTO_INCREMENT PRIMARY KEY, categoryId INT,
                       dateOf DATE, start TIME, end TIME)
                       ''')

cursor.execute('''
    CREATE TABLE Money(id INT AUTO_INCREMENT PRIMARY KEY, categoryId INT,
                       amount INT, dateOf DATE)
                       ''')

cursor.execute('''
    CREATE TABLE Once(id INT AUTO_INCREMENT PRIMARY KEY, categoryId INT,
                       dateOf DATE)
                       ''')

cursor.execute('''
    CREATE TABLE Pot(id INT AUTO_INCREMENT PRIMARY KEY, categoryId INT,
                       amount INT, dateOf DATE, startDate Date, endDate Date,
                       repeats BOOLEAN)
                       ''')

cursor.execute('''
    CREATE TABLE Transaction(id INT AUTO_INCREMENT PRIMARY KEY, potId INT,
                       userId INT, amount INT, dateOf Date)
                       ''')

# user

params = ('Xavier', 'gAAAAABcAEWIqijwIP1xIemm1F3474aOx9lS-UWRI11IAh8Kvn0NfS2Lsu_h55g8Jx2RbLfhnUwUg5_-XrQkfj9PJrSAR47x5Q==')
cursor = connection.cursor()
cursor.execute('INSERT INTO User (name, password) VALUES(%s, %s)', params)

# categorie
params = (1, 'werken', True, False, False, False, 1)
cursor = connection.cursor()
cursor.execute('INSERT INTO Category (userId, name, time, money, once, pot, points) VALUES(%s, %s, %s, %s, %s, %s, %s)', params)

params = (1, 'roken', False, True, False, False, -3)
cursor.execute('INSERT INTO Category (userId, name, time, money, once, pot, points) VALUES(%s, %s, %s, %s, %s, %s, %s)', params)

params = (1, 'ochtend_sporten', False, False, True, False, 2)
cursor.execute('INSERT INTO Category (userId, name, time, money, once, pot, points) VALUES(%s, %s, %s, %s, %s, %s, %s)', params)

params = (1, 'fitness', False, False, True, False, 3)
cursor.execute('INSERT INTO Category (userId, name, time, money, once, pot, points) VALUES(%s, %s, %s, %s, %s, %s, %s)', params)

params = (1, 'Huishoudelijke Pot', False, False, False, True, 1)
cursor.execute('INSERT INTO Category (userId, name, time, money, once, pot, points) VALUES(%s, %s, %s, %s, %s, %s, %s)', params)

# pot
params = (5, 0, '2018/11/19', '2018/11/19', '2018/12/16')
cursor.execute('INSERT INTO Pot (categoryId, amount, dateOf, startDate, endDate) VALUES(%s, %s, %s, %s, %s)', params)


# # once
# params = (3, '2018-11-19')
# cursor.execute('INSERT INTO once (categoryId, dateOf) VALUES(%s, %s)', params)

# params = (4, '2018-11-19')
# cursor.execute('INSERT INTO once (categoryId, dateOf) VALUES(%s, %s)', params)

# params = (4, '2018-11-20')
# cursor.execute('INSERT INTO once (categoryId, dateOf) VALUES(%s, %s)', params)

# params = (3, '2018-11-21')
# cursor.execute('INSERT INTO once (categoryId, dateOf) VALUES(%s, %s)', params)

# params = (4, '2018-11-21')
# cursor.execute('INSERT INTO once (categoryId, dateOf) VALUES(%s, %s)', params)

# params = (3, '2018-11-22')
# cursor.execute('INSERT INTO once (categoryId, dateOf) VALUES(%s, %s)', params)

# params = (4, '2018-11-22')
# cursor.execute('INSERT INTO once (categoryId, dateOf) VALUES(%s, %s)', params)

# params = (4, '2018-11-23')
# cursor.execute('INSERT INTO once (categoryId, dateOf) VALUES(%s, %s)', params)

# params = (3, '2018-11-24')
# cursor.execute('INSERT INTO once (categoryId, dateOf) VALUES(%s, %s)', params)

# params = (3, '2018-11-25')
# cursor.execute('INSERT INTO once (categoryId, dateOf) VALUES(%s, %s)', params)

# # money
# dt = datetime.strptime('2018-10-1', '%Y-%m-%d')
# for i in range(1, 100):
#     params = (2, i, dt.strftime('%Y-%m-%d'))
#     cursor.execute('INSERT INTO money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)
#     dt += timedelta(days=1)

# # params = (2, 10, '2018-11-17')
# # cursor.execute('INSERT INTO money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)

# # params = (2, 10, '2018-11-18')
# # cursor.execute('INSERT INTO money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)

# # params = (2, 10, '2018-11-19')
# # cursor.execute('INSERT INTO money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)

# # params = (2, 10, '2018-11-20')
# # cursor.execute('INSERT INTO money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)

# # params = (2, 10, '2018-11-22')
# # cursor.execute('INSERT INTO money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)

# # params = (2, 10, '2018-11-23')
# # cursor.execute('INSERT INTO money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)

# # params = (2, 10, '2018-11-24')
# # cursor.execute('INSERT INTO money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)

# # params = (2, 10, '2018-11-25')
# # cursor.execute('INSERT INTO money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)

# # params = (2, 10, '2018-11-26')
# # cursor.execute('INSERT INTO money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)

# # params = (2, 10, '2018-11-27')
# # cursor.execute('INSERT INTO money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)

# # params = (2, 10, '2018-11-28')
# # cursor.execute('INSERT INTO money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)

# # params = (2, 10, '2018-11-29')
# # cursor.execute('INSERT INTO money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)

# # params = (2, 10, '2018-11-30')
# # cursor.execute('INSERT INTO money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)

# # params = (2, 10, '2018-12-1')
# # cursor.execute('INSERT INTO money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)

# # params = (2, 10, '2018-12-2')
# # cursor.execute('INSERT INTO money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)

# # params = (2, 10, '2018-12-3')
# # cursor.execute('INSERT INTO money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)

# # params = (2, 10, '2018-12-4')
# # cursor.execute('INSERT INTO money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)

# # params = (2, 10, '2018-12-5')
# # cursor.execute('INSERT INTO money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)


# # time
# params = (1, '2018-11-17', '9:00:00', '13:00:00')
# cursor.execute('INSERT INTO time (categoryId, dateOf, start, end) VALUES(%s, %s, %s, %s)', params)

# params = (1, '2018-11-18', '9:00:00', '13:00:00')
# cursor.execute('INSERT INTO time (categoryId, dateOf, start, end) VALUES(%s, %s, %s, %s)', params)

# params = (1, '2018-11-19', '9:00:00', '13:00:00')
# cursor.execute('INSERT INTO time (categoryId, dateOf, start, end) VALUES(%s, %s, %s, %s)', params)

# params = (1, '2018-11-19', '15:23:12', '17:54:45')
# cursor.execute('INSERT INTO time (categoryId, dateOf, start, end) VALUES(%s, %s, %s, %s)', params)

# params = (1, '2018-11-20', '9:00:00', '13:00:00')
# cursor.execute('INSERT INTO time (categoryId, dateOf, start, end) VALUES(%s, %s, %s, %s)', params)

# params = (1, '2018-11-20', '15:23:12', '17:54:45')
# cursor.execute('INSERT INTO time (categoryId, dateOf, start, end) VALUES(%s, %s, %s, %s)', params)

# params = (1, '2018-11-21', '9:00:00', '13:00:00')
# cursor.execute('INSERT INTO time (categoryId, dateOf, start, end) VALUES(%s, %s, %s, %s)', params)

# params = (1, '2018-11-21', '15:23:12', '17:54:45')
# cursor.execute('INSERT INTO time (categoryId, dateOf, start, end) VALUES(%s, %s, %s, %s)', params)

# params = (1, '2018-11-22', '9:00:00', '13:00:00')
# cursor.execute('INSERT INTO time (categoryId, dateOf, start, end) VALUES(%s, %s, %s, %s)', params)

# params = (1, '2018-11-22', '15:23:12', '17:54:45')
# cursor.execute('INSERT INTO time (categoryId, dateOf, start, end) VALUES(%s, %s, %s, %s)', params)

# params = (1, '2018-11-23', '9:00:00', '13:00:00')
# cursor.execute('INSERT INTO time (categoryId, dateOf, start, end) VALUES(%s, %s, %s, %s)', params)

# params = (1, '2018-11-23', '15:23:12', '17:54:45')
# cursor.execute('INSERT INTO time (categoryId, dateOf, start, end) VALUES(%s, %s, %s, %s)', params)

# params = (1, '2018-11-24', '9:00:00', '13:00:00')
# cursor.execute('INSERT INTO time (categoryId, dateOf, start, end) VALUES(%s, %s, %s, %s)', params)

# params = (1, '2018-11-26', '9:00:00', '13:00:00')
# cursor.execute('INSERT INTO time (categoryId, dateOf, start, end) VALUES(%s, %s, %s, %s)', params)

# params = (1, '2018-11-27', '9:00:00', '13:00:00')
# cursor.execute('INSERT INTO time (categoryId, dateOf, start, end) VALUES(%s, %s, %s, %s)', params)

# commit changes
connection.commit()
# close database
connection.close()