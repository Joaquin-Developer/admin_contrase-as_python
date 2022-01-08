import utils
import core.config as cfg
import tkinter as tk
from tkinter import *


def init(): 
    """ Inicializamos la GUI y cargamos los archivos de configuracion """
    root = tk.Tk()
    root.title(cfg.APP_NAME)
    app = App(master=root)
    app.mainloop()


def update_value(data: dict):
    """ 
    Modificar el valor de un registro de contraseñas 
    Los campos del duccionario data:
        - index: int
        - site: str
        - username: str
        - password: str
    """
    # llamar a utils, buscar el elemento en la lista de contaseñas
    # modificarlo, y luego sobreescribir el archivo json: data/my_keys.json


class App(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hola mundo\n(dame click)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        self.quit = tk.Button(self, text="Salir", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("Hola mundo")


if __name__ == "__main__":
    init()
