from controller.LoginController import LoginController
from entity.UsuarioEntity import UsuarioEntity

from utils.GuiUtils import GuiUtils
import getpass


class LoginGui:
    
    def __init__(self):
        self.usuarioController  = LoginController()
    
    def login(self):
        print("Por Favor Ingrese sus Credenciales")

        usuario = input("Usuario:")
        password =  getpass.getpass()
        us = self.usuarioController.login(usuario,password)
        if(us):
            GuiUtils.clearTerminal()
            print("Bienvenido %s"% us.nombreUsuario)
        else:
            print("Credenciales Incorrectas... intente nuevamente") 
        return us
          