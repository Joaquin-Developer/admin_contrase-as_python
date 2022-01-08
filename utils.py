import cryptography
from cryptography.fernet import Fernet

KEY_PATH = "data/key.key"
DATA_PATH = "data/my_keys.json"

def read_file(path, args="r") -> str:
    with open(path, args) as file:
        data = file.read()
    return data


def write_file(path, args, data) -> None:
    with open(path, args) as file:
        file.write(data)


def generate_key() -> bytes:
    key = Fernet.generate_key()
    # with open(KEY_PATH, "wb") as file:
    #     file.write(key)
    write_file(KEY_PATH, "wb", key)
    return key


def get_key() -> bytes:
    # with open(KEY_PATH) as filekey:
    #     key = filekey.read()
    key = read_file(KEY_PATH)
    
    if key is None: # or len(key) == 0: 
        return generate_key()
    return key


def encrypt_and_save(path: str):
    fernet = Fernet(get_key())
    # with open(path, "rb") as file:
    #     data = file.read()
    data = read_file(path, args="rb")
    encrypted_data = fernet.encrypt(data)
    # with open(path, "wb") as encrypted_file:
    #     encrypted_file.write(encrypted_data)
    write_file(path, "wb", encrypted_data)


def decrypt(path: str):
    fernet = Fernet(get_key())
    encrypted_data = read_file(path, args="rb")
    decrypted_data = fernet.decrypt(encrypted_data)
    return decrypted_data

