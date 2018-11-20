import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='Xavier3153',
        database='tracking',
        auth_plugin='mysql_native_password'
    )