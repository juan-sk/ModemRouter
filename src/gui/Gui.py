from gui.LoginGui import LoginGui
from gui.jefemesa.JefeMesa import JefeMesa
from service.UsuarioService import UsuarioService
from utils.GuiUtils import GuiUtils


class Gui:
    
    def __init__(self):
        self.loginGui = LoginGui()
        pass
    def mensajeBienvenida(self):
        GuiUtils.clearTerminal()
        print("Inicia la aplicacion")
        print("Bienvenido..")
        
        
    def gui(self):
        self.mensajeBienvenida()
        usuario = self.loginGui.login()
        if usuario.idTipoUsuario == 1:
            # usuario jefe de mesa
            print ("inciar gui de jefe de mesa")
            JefeMesa().start()
        elif usuario.idTipoUsuario ==2:
            print ("inciar gui de ejecutvo de mesa")
        elif usuario.idTipoUsuario ==3:
            print ("inciar gui de ejecutvo especialista")
            