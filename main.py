import utils
import core.config as cfg
import tkinter as tk
from tkinter import ttk
from tkinter import *


def init(): 
    """ Inicializamos la GUI y cargamos los archivos de configuracion """
    root = tk.Tk()
    root.title(cfg.APP_NAME)
    root.geometry(cfg.gui["size"]["window"])

    app = App(master=root)
    app.mainloop()


def update_and_save_value(data: dict):
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


def get_values() -> tuple:
    return "Hola", "Chau"


def get_specific_value(name) -> dict:
    pass


class App(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # label for select:
        self.lbl_title = tk.Label(self, 
                        text=cfg.gui["lbl_title"],
                        font=("Arial Bold", 12))
        self.lbl_title.grid(column=0, row=0)

        self.cbox_list_passwords = ttk.Combobox(self)
        self.cbox_list_passwords["values"] = get_values()
        self.cbox_list_passwords.grid(column=1, row=0)
        self.cbox_list_passwords.bind("<<ComboboxSelected>>", self.update_value)

        # Agregar botón para modificar...
        """
        Funciones a implementar:
            - Agregar contraseñas
            - Update contraseñas (nombre, red, contraseña)
            - Eliminar contraseñas
        """

        # Panel:
        # self.panel_update_values = tk.PanedWindow(bd=4, relief="raised", bg="green")
        self.panel_update_values = tk.PanedWindow()
        
        self.panel_update_values.pack()
        label_title_panel = Label(self.panel_update_values, text="Setear valores:")
        # label_title_panel.grid(column=0, row=0)
        self.panel_update_values.add(label_title_panel)

        entry_site = tk.Entry(self.panel_update_values)
        entry_username = tk.Entry(self.panel_update_values)
        entry_password = tk.Entry(self.panel_update_values)
        self.panel_update_values.add(entry_site)
        self.panel_update_values.add(entry_username)
        self.panel_update_values.add(entry_password)

    def update_selected_value(self):
        pass

    def update_value(self, event):
        # Mostrar un MessageBox para setear los valores, y guardarlos.
        name = self.cbox_list_passwords.get()
        print("Cambió el elemento seleccionado", name)
        name = name.split(" - ")[0]
        data = get_specific_value(name)
        update_and_save_value(data)


if __name__ == "__main__":
    init()
