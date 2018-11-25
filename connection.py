import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host='****',
        user='****',
        passwd='****',
        database='****',
        auth_plugin='mysql_native_password'
        )   
