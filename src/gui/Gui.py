from gui.LoginGui import LoginGui
from service.UsuarioService import UsuarioService


class Gui:
    
    def __init__(self):
        self.loginGui = LoginGui()
        pass
    def mensajeBienvenida(self):
        print("Inicia la aplicacion")
        print("Bienvenido..")
        
        
    def gui(self):
        self.mensajeBienvenida()
        self.loginGui.login()