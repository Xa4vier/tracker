from cryptography.fernet import Fernet

from database.insert import insert_user
from database.get import select_user_by_name

def create_user(name, password):
    password = decrypt_password(password)
    insert_user(name, password)
    return 'succes'

def get_user(name, password):
    user = select_user_by_name(name)
    if password == encrypt_password(str.encode(user[2])):
        message = user
    else :
        message = 'User not found'
    return message
    

def decrypt_password(password):
    key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(str.encode(password))

def encrypt_password(password):
    key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
    cipher_suite = Fernet(key)
    uncipher_text = (cipher_suite.decrypt(password))
    return bytes(uncipher_text).decode("utf-8") #convert to string