from database.connection import create_connection

def get_connection():
    return create_connection()

### user ###

def select_user_by_name(name):
    params = (name,)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute = cursor.execute
    cursor.execute("SELECT * FROM User WHERE name = %s", params)
    return cursor.fetchone()

def select_user_by_id(userId):
    params = (userId,)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute = cursor.execute
    cursor.execute("SELECT * FROM User WHERE id = %s", params)
    return cursor.fetchone()

### user group ###

def select_usergroup_by_user_group_id(userId, groupId):
    params = (userId, groupId)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute = cursor.execute
    cursor.execute("SELECT * FROM UserGroup WHERE userId = %s AND groupId = %s", params)
    return cursor.fetchall()

### groups ###

# select all groups of the user if the user is a admin
def select_groups_admin_id(userId):
    params = (userId,)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute = cursor.execute
    cursor.execute('''SELECT g.id, g.name FROM GroupsOf AS g
    INNER JOIN Admin AS a
    ON g.Id = a.groupId
    INNER JOIN User AS u
    ON a.userId = u.id
    WHERE a.userId = %s''', params)
    return cursor.fetchall()

# select a specific group of the user if the user is a admin 
def select_groups_admin_id_group_id(userId, groupId):
    params = (userId, groupId)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute = cursor.execute
    cursor.execute('''SELECT g.id, g.name FROM GroupsOf AS g
    INNER JOIN Admin AS a
    ON g.Id = a.groupId
    INNER JOIN User AS u
    ON a.userId = u.id
    WHERE a.userId = %s
    AND g.Id = %s''', params)
    return cursor.fetchall()

### category ###

def select_all_category_names(userId):
    params = (userId,)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT name FROM Category WHERE userId = %s', params)
    return cursor.fetchall()

def select_all_from_category_by_userId(userId):
    params = (userId,)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Category WHERE userId = %s', params)
    return cursor.fetchall()

def select_category_by_id(userId, categoryId):
    params = (userId, categoryId)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Category WHERE userId = %s AND id = %s', params)
    return cursor.fetchone()

### once ###

def select_once_by_cid_and_date(id, date):
    params = (id, date)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Once WHERE categoryId = %s AND dateOf = '%s'", params)
    return cursor.fetchall()

def select_once_by_start_end(categoryId, start, end):
    params = (categoryId, start, end)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute = cursor.execute
    p = "SELECT * FROM Once WHERE categoryId = %s AND dateOf >= %s AND dateOf <= %s", params
    cursor.execute("SELECT * FROM Once WHERE categoryId = %s AND dateOf >= %s AND dateOf <= %s", params)
    return cursor.fetchall()

### money ###

def select_money_by_start_end(categoryId, start, end):
    params = (categoryId, start, end)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Money WHERE categoryId = %s AND dateOf >= %s AND dateOf <= %s", params)
    return cursor.fetchall()

### time ###

def select_time_by_date_endtime_cid(id, date):
    params = (id, date)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Time WHERE categoryId = %s AND end IS NULL AND dateOf = %s", params)
    return cursor.fetchall()

def select_time_by_start_end(categoryId, start, end):
    params = (categoryId, start, end)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Time WHERE categoryId = %s AND dateOf >= %s AND dateOf <= %s", params)
    return cursor.fetchall()

def select_pot_by_categoryId(categoryId):
    params = (categoryId,)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pot WHERE categoryId = %s", params)
    return cursor.fetchone() 