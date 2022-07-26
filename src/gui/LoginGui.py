from asyncio.log import logger
from controller.LoginController import LoginController
from entity.UsuarioEntity import UsuarioEntity
import logging

from utils.GuiUtils import GuiUtils
import getpass


class LoginGui:
    
    def __init__(self):
        self.usuarioController  = LoginController()
    
    def login(self):
        GuiUtils.subtitulo("Inicio de sesión: ingrese su usuario y contraseña")
        usuario = input(" Usuario: ")
        password =  getpass.getpass(" Contraseña: ")
        us = self.usuarioController.login(usuario,password)
        if(us):
            return us
        else:
            logging.error("Credenciales Incorrectas... intente nuevamente") 
          