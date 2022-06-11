from controller.LoginController import LoginController
from entity.UsuarioEntity import UsuarioEntity
from utils.GuiUtils import GuiUtils
import getpass


class LoginGui:
    
    def __init__(self):
        self.usuarioController  = LoginController()
    
    def login(self):
        print("Por Favor Ingrese sus Credenciales")

        usuario = UsuarioEntity()
        while True:
            usuario = input("Usuario:")
            password =  getpass.getpass()
            
            usuario = self.usuarioController.login(usuario,password)
            if(usuario):
                GuiUtils.clearTerminal()
                print("Bienvenido %s"% usuario.nombreUsuario)
                break
            else:
                print("Credenciales Incorrectas... intente nuevamente")
        return usuario
          