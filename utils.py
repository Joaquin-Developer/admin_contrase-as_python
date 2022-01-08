import cryptography
from cryptography.fernet import Fernet

KEY_PATH = "data/key.key"

def get_file(path):
    pass


def generate_key() -> bytes:
    key = Fernet.generate_key()
    with open(KEY_PATH, "wb") as file:
        file.write(key)
    return key


def get_key():
    with open(KEY_PATH) as file:
        key = file.read()
    
    if key is None: # or len(key) == 0:
        return generate_key()
    return key


def encrypt(path: str):
    pass


def decrypt(path: str):
    pass


