from connection import create_connection

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
params = ('werken', True, False, False, 1)
cursor = connection.cursor()
cursor.execute('INSERT INTO category (name, time, money, once, points) VALUES(%s, %s, %s, %s, %s)', params)

params = ('wiet_roken', False, True, False, 3)
cursor.execute('INSERT INTO category (name, time, money, once, points) VALUES(%s, %s, %s, %s, %s)', params)

params = ('ochtend_sporten', False, False, True, 2)
cursor.execute('INSERT INTO category (name, time, money, once, points) VALUES(%s, %s, %s, %s, %s)', params)

params = ('fitness', False, False, True, 3)
cursor.execute('INSERT INTO category (name, time, money, once, points) VALUES(%s, %s, %s, %s, %s)', params)

# once
params = (3, '2018-11-19')
cursor.execute('INSERT INTO once (categoryId, dateOf) VALUES(%s, %s)', params)

params = (4, '2018-11-19')
cursor.execute('INSERT INTO once (categoryId, dateOf) VALUES(%s, %s)', params)

params = (4, '2018-11-20')
cursor.execute('INSERT INTO once (categoryId, dateOf) VALUES(%s, %s)', params)

params = (3, '2018-11-21')
cursor.execute('INSERT INTO once (categoryId, dateOf) VALUES(%s, %s)', params)

params = (4, '2018-11-21')
cursor.execute('INSERT INTO once (categoryId, dateOf) VALUES(%s, %s)', params)

params = (3, '2018-11-22')
cursor.execute('INSERT INTO once (categoryId, dateOf) VALUES(%s, %s)', params)

params = (4, '2018-11-22')
cursor.execute('INSERT INTO once (categoryId, dateOf) VALUES(%s, %s)', params)

params = (4, '2018-11-23')
cursor.execute('INSERT INTO once (categoryId, dateOf) VALUES(%s, %s)', params)

params = (3, '2018-11-24')
cursor.execute('INSERT INTO once (categoryId, dateOf) VALUES(%s, %s)', params)

params = (3, '2018-11-25')
cursor.execute('INSERT INTO once (categoryId, dateOf) VALUES(%s, %s)', params)

# money
params = (3, 10, '2018-11-19')
cursor.execute('INSERT INTO money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)

params = (3, 10, '2018-11-20')
cursor.execute('INSERT INTO money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)

params = (3, 10, '2018-11-22')
cursor.execute('INSERT INTO money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)

params = (3, 10, '2018-11-23')
cursor.execute('INSERT INTO money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)

params = (3, 10, '2018-11-24')
cursor.execute('INSERT INTO money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)

params = (3, 10, '2018-11-25')
cursor.execute('INSERT INTO money (categoryId, amount, dateOf) VALUES(%s, %s, %s)', params)

# time
params = (3, '2018-11-19', '9:00:00', '13:00:00')
cursor.execute('INSERT INTO time (categoryId, dateOf, start, end) VALUES(%s, %s, %s, %s)', params)

params = (3, '2018-11-24', '15:23:12', '17:54:45')
cursor.execute('INSERT INTO time (categoryId, dateOf, start, end) VALUES(%s, %s, %s, %s)', params)

params = (3, '2018-11-20', '9:00:00', '13:00:00')
cursor.execute('INSERT INTO time (categoryId, dateOf, start, end) VALUES(%s, %s, %s, %s)', params)

params = (3, '2018-11-24', '15:23:12', '17:54:45')
cursor.execute('INSERT INTO time (categoryId, dateOf, start, end) VALUES(%s, %s, %s, %s)', params)

params = (3, '2018-11-21', '9:00:00', '13:00:00')
cursor.execute('INSERT INTO time (categoryId, dateOf, start, end) VALUES(%s, %s, %s, %s)', params)

params = (3, '2018-11-24', '15:23:12', '17:54:45')
cursor.execute('INSERT INTO time (categoryId, dateOf, start, end) VALUES(%s, %s, %s, %s)', params)

params = (3, '2018-11-22', '9:00:00', '13:00:00')
cursor.execute('INSERT INTO time (categoryId, dateOf, start, end) VALUES(%s, %s, %s, %s)', params)

params = (3, '2018-11-24', '15:23:12', '17:54:45')
cursor.execute('INSERT INTO time (categoryId, dateOf, start, end) VALUES(%s, %s, %s, %s)', params)

params = (3, '2018-11-23', '9:00:00', '13:00:00')
cursor.execute('INSERT INTO time (categoryId, dateOf, start, end) VALUES(%s, %s, %s, %s)', params)

params = (3, '2018-11-24', '15:23:12', '17:54:45')
cursor.execute('INSERT INTO time (categoryId, dateOf, start, end) VALUES(%s, %s, %s, %s)', params)

params = (3, '2018-11-24', '9:00:00', '13:00:00')
cursor.execute('INSERT INTO time (categoryId, dateOf, start, end) VALUES(%s, %s, %s, %s)', params)

# commit changes
connection.commit()
# close database
connection.close()