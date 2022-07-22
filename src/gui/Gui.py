import logging
from gui.LoginGui import LoginGui
from gui.ejecutivoEspecifico.EjecutivoEspecifico import EjecutivoEspecifico
from gui.ejecutivomesa.EjecutivoMesa import EjecutivoMesa
from gui.jefemesa.JefeMesa import JefeMesa
from service.UsuarioService import UsuarioService
from utils.GuiUtils import GuiUtils


class Gui:
    
    def __init__(self):
        self.loginGui = LoginGui()
        pass

    def mensajeBienvenida(self):
        GuiUtils.clearTerminal()
        print(GuiUtils.subrrayar("Software TMA"))
        print()

    def gui(self):
        self.mensajeBienvenida()
        usuario = self.loginGui.login()
        if(usuario):
            # idUsuario =  usuario.id
            if usuario.idTipoUsuario == 1:
                # usuario jefe de mesa
                # print ("inciar gui de jefe de mesa")
                JefeMesa().start()
            elif usuario.idTipoUsuario == 2:
                # print ("inciar gui de ejecutvo de mesa")
                EjecutivoMesa().start(usuario.id)
            elif usuario.idTipoUsuario == 3:
                # print ("inciar gui de ejecutvo especialista")
                EjecutivoEspecifico().start(usuario.id)
                
        # print("Hasta luego %s"%usuario.nombreUsuario)
