from connection import create_connection
from datetime import *

# Get a cursor object
connection = create_connection()
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE category(id INT AUTO_INCREMENT PRIMARY KEY, name TEXT,
                       time BOOLEAN, money BOOLEAN, once BOOLEAN, points INTEGER)
''')

cursor.execute('''
    CREATE TABLE time(id INT AUTO_INCREMENT PRIMARY KEY, categoryId INTEGER,
                       dateOf DATE, start TIME, end TIME)
''')

cursor.execute('''
    CREATE TABLE money(id INT AUTO_INCREMENT PRIMARY KEY, categoryId INTEGER,
                       amount INTEGER, dateOf DATE)
''')

cursor.execute('''
    CREATE TABLE once(id INT AUTO_INCREMENT PRIMARY KEY, categoryId INTEGER,
                       dateOf DATE)
''')

# categorie
params = ('werken', True, False, False, False, 1)
cursor = connection.cursor()
cursor.execute('INSERT INTO category (name, time, money, once, pot, points) VALUES(%s, %s, %s, %s, %s, %s)', params)

params = ('roken', False, True, False, False, -3)
cursor.execute('INSERT INTO category (name, time, money, once, pot, points) VALUES(%s, %s, %s, %s, %s, %s)', params)

params = ('ochtend_sporten', False, False, True, False, 2)
cursor.execute('INSERT INTO category (name, time, money, once, pot, points) VALUES(%s, %s, %s, %s, %s, %s)', params)

params = ('fitness', False, False, True, False, 3)
cursor.execute('INSERT INTO category (name, time, money, once, pot, points) VALUES(%s, %s, %s, %s, %s, %s)', params)

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