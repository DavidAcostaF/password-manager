from cryptography.fernet import Fernet

from dotenv import load_dotenv
import os

load_dotenv()

def encrypt(password):
    key = os.getenv("secret_key").encode()
    f = Fernet(key)
    encrypted = f.encrypt(password.encode())
    return encrypted.decode()
        
def decrypt(password_encrypted):
    key = os.getenv("secret_key").encode()
    f = Fernet(key)
    decrypted = f.decrypt(password_encrypted).decode()

    return decrypted