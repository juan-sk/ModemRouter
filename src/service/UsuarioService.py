from logging import exception
import logging
from config.Config import Config
from entity.AreaUsuarioEntity import AreaUsuarioEntity
from entity.UsuarioEntity import UsuarioEntity
from repository.AreaRepository import AreaRepository
from repository.AreaUsuarioReposotory import AreaUsuarioReposotory
from repository.UsuarioRepository import UsuarioRepository


class UsuarioService:
    
    
    def __init__(self):
        self.usuarioRepo = UsuarioRepository()
        self.areaRepo = AreaRepository()
        self.areaUsuarioRepo = AreaUsuarioReposotory()
        self._dbConn = Config().DBConnection
        
    def validarusuario(self, usaurio,password):
        try:
            return self.usuarioRepo.obtenerUsuarioByUsuarioAndPass(usaurio,password)
        except Exception as error:
            logging.error("ocurrio un error al validar las credenciales del usuario")
            logging.error(error)
            raise error
        
        
        
    def guardarUsuario(self,usuario):
        try:

            usuarioEntity = UsuarioEntity.fromUsuario(usuario)
            
            cursor = self._dbConn.cursor()
            self.usuarioRepo.guardarUsuario(cursor, usuarioEntity)
            
            if usuario.idArea ==3:
                areaUsuarioEntity =AreaUsuarioEntity.fromUsuario(usuario)
                areaUsuarioEntity.idUsuario = cursor.lastrowid#obteiene el id del registro insertado
                self.areaUsuarioRepo.guardarAreaUsuario(cursor,areaUsuarioEntity)
            
        
            self._dbConn.commit()  
            cursor.close()  
        except Exception as error:
            logging.error("ocurrio un error guardando el usuario")
            logging.error(error)
            self._dbConn.rollback()
            cursor.close()  
            raise error
        
        
    def obtenerArea (self):
        return self.areaRepo.obtenerAreas();
        