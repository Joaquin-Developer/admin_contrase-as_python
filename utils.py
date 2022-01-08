import cryptography
from cryptography.fernet import Fernet

KEY_PATH = "data/key.key"
DATA_PATH = "data/my_keys.json"

def get_file(path):
    pass


def generate_key() -> bytes:
    key = Fernet.generate_key()
    with open(KEY_PATH, "wb") as file:
        file.write(key)
    return key


def get_key() -> bytes:
    with open(KEY_PATH) as file:
        key = file.read()
    
    if key is None: # or len(key) == 0: 
        return generate_key()
    return key


def encrypt(path: str):
    with open(KEY_PATH, "rb") as filekey:
        key = filekey.read()
    
    fernet = Fernet(key)

    with open(DATA_PATH, "rb") as file:
        data = file.read()
    encrypted_data = fernet.encrypt(data)

    with open(DATA_PATH, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)


def decrypt(path: str):
    pass


