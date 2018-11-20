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
                       amount INTEGER)
''')

cursor.execute('''
    CREATE TABLE once(id INT AUTO_INCREMENT PRIMARY KEY, categoryId INTEGER,
                       dateOf DATE)
''')

params = ('werken', True, False, False, 1)
cursor = connection.cursor()
cursor.execute('INSERT INTO category (name, time, money, once, points) VALUES(%s, %s, %s, %s, %s)', params)

params = ('wiet_roken', False, True, False, 3)
cursor.execute('INSERT INTO category (name, time, money, once, points) VALUES(%s, %s, %s, %s, %s)', params)

params = ('ochtend_sporten', False, False, True, 2)
cursor.execute('INSERT INTO category (name, time, money, once, points) VALUES(%s, %s, %s, %s, %s)', params)

params = ('fitniss', False, False, True, 3)
cursor.execute('INSERT INTO category (name, time, money, once, points) VALUES(%s, %s, %s, %s, %s)', params)

# commit changes
connection.commit()
# close database
connection.close()