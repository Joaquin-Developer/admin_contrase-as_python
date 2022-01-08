import utils
import json


def main():
    # datos de prueba:
    data = [
        {
            "index": 0,
            "site": "instagram",
            "username": "Joaquin12345",
            "password": "12345"
        },
        {
            "index": 1,
            "site": "correo gmail",
            "username": "usuario@gmail.com",
            "password": "67890"
        }
    ]
    # texto a json:
    json_data = json.dumps(data)
    print(json_data)
    print(type(json_data))
    # reconvertir: json a texto:
    data_original = json.loads(json_data)
    print(data_original)
    print(type(data_original))


def load():
    data = utils.read_file("data/test.json")
    
    print(data)
    json_data = json.loads(data)
    print(json_data)
    print(type(json_data))

if __name__ == "__main__":
    load()