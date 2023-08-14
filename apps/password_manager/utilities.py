from cryptography.fernet import Fernet

def encrypt(password):
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted = f.encrypt(password.encode())
    return encrypted
        
def decrypt(password):
    key = Fernet.generate_key()
    f = Fernet(key)
    decrypted = f.decrypt(password.encode())
    return decrypted