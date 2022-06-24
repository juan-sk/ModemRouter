import logging
from service.TipoUsuarioService import TipoUsuarioService
from service.UsuarioService import UsuarioService


class JefeDeMesaController:
    
        
    def __init__(self) :
        self.tipoUsuarioService = TipoUsuarioService()
        self.usuarioService = UsuarioService()
        pass
    
    def obtenerTiposUsuario(self):
        try:
            logging.info("se inicia la obtencion de tipos de usuario")
            tiposUsuario=  self.usuarioService.obtenerTiposDeUsuario()
            logging.info("se termina la obtencion de tipos de usuario")
            return tiposUsuario
        except Exception as error:
            logging.error(error)
            # se retorna null 
            pass
    def obtenerAreas(self):
        try:
            
            areas = self.usuarioService.obtenerArea()
            return areas
        except Exception as error:
            logging.error("ocurrio un error al obtener las areas")
            logging.error(error)
    def guardarUsuario(self,usuario):
        try:
            self.usuarioService.guardarUsuario(usuario)
            return 1
        except Exception as error :
            logging.error("ocurrio un error guardando el usuario")
            logging.error (error)
            return -1