import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host='localhost',
        user='XavierDev',
        passwd='Test1@',
        database='tracker',
        #auth_plugin='mysql_native_password'
        )