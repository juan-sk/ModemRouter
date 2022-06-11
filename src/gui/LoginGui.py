from controller.LoginController import LoginController
from entity.UsuarioEntity import UsuarioEntity
from utils.GuiUtils import GuiUtils


class LoginGui:
    
    def __init__(self):
        self.usuarioController  = LoginController()
    
    def login(self):
        print("Porfavor ingrese sus credenciales")

        usuario = UsuarioEntity()
        while True:
            usuario = input("Usuario:")
            password =input("Password:")
            
            usuario = self.usuarioController.login(usuario,password)
            if(usuario):
                GuiUtils.clearTerminal()
                print("Bienvenido %s"% usuario.nombreUsuario)
                break
        return usuario
          