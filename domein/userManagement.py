from database.insert import insert_user
from cryptography.fernet import Fernet

def create_account(name, password):
    password = encrypt_password(password)
    insert_user(name, password)
    return 'succes'

def encrypt_password(password):
    key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(str.encode(password))

def decrypt_password(password):
    key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
    cipher_suite = Fernet(key)
    uncipher_text = (cipher_suite.decrypt(password))
    return bytes(uncipher_text).decode("utf-8") #convert to string