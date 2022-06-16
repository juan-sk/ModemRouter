from logging import exception
import logging
from repository.UsuarioRepository import UsuarioRepository


class UsuarioService:
    
    
    def __init__(self):
        self.usuarioRepo = UsuarioRepository() 
        
    def validarusuario(self, usaurio,password):
        try:
            return self.usuarioRepo.obtenerUsuarioByUsuarioAndPass(usaurio,password)
        except Exception as error:
            logging.error("ocurrio un error al validar las credenciales del usuario")
            logging.error(error)
            raise error
    def guardarUsuario(self,usuario):
        self.usuarioRepo.guardarUsuario(usuario)
        