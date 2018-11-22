from connection import create_connection

def get_connection():
    return create_connection()

def update_time_end(categoryId, dateOf, end):
    params = (end, categoryId, dateOf)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('UPDATE time SET end = %s WHERE categoryId = %s AND dateOf = %s AND IS NULL', params)
    connection.commit()
    connection.close()

def delete():
    pass





# sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"