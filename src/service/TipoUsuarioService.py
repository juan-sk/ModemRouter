import logging
from repository.TipoUsuarioRepository import TipoUsuarioRepository
from repository.UsuarioRepository import UsuarioRepository


class TipoUsuarioService:
    
    def __init__(self):
        self.tipoTiketRepo = TipoUsuarioRepository()
        self.usuarioRepo = UsuarioRepository()
        
    def obtenerTiposDeUsuario(self):
        
        try:
            tiposUsuario = self.tipoTiketRepo.obtenerTipoUsuarios()
            return tiposUsuario
        except Exception as error:
            logging.error("ocurrio un error en el servicio al obtener los tipos de usuario")
            logging.error(error)
            return []

        
        
        
        
        