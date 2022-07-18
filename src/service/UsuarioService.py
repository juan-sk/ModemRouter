
import logging
from config.Config import Config
from entity.AreaUsuarioEntity import AreaUsuarioEntity
from entity.UsuarioEntity import UsuarioEntity
from pojo.Usuario import Usuario
from repository.AreaRepository import AreaRepository
from repository.AreaUsuarioReposotory import AreaUsuarioReposotory
from repository.TipoUsuarioRepository import TipoUsuarioRepository
from repository.UsuarioRepository import UsuarioRepository


class UsuarioService:
    
    
    def __init__(self):
        self.usuarioRepo = UsuarioRepository._usuarioRepository
        self.areaRepo = AreaRepository._areaRepository
        self.areaUsuarioRepo = AreaUsuarioReposotory._areaUsuarioReposotory
        self.tipoUsuario = TipoUsuarioRepository._tipoUsuarioRepository
        self._dbConn = Config._dbConnection
        
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
    
        
    def obtenerTiposDeUsuario(self):
        
        try:
            tiposUsuario = self.tipoUsuario.obtenerTipoUsuarios()
            return tiposUsuario
        except Exception as error:
            logging.error("ocurrio un error en el servicio al obtener los tipos de usuario")
            logging.error(error)
            return []
        
    def obtenerUusarios(self):
        # obtener tipos de usuario
        tiposUsuario =  self.tipoUsuario.obtenerTipoUsuarios()
        us = []
        # obtener usuarios
        usuariosDB = self.usuarioRepo.obtenerUsuarios()
        for udb in usuariosDB:
            area = self.areaRepo.obtenerAreaUsuaio(udb.id)
            u = Usuario.fromUsuario(udb,tiposUsuario,area)
            us.append(u)        
        return us
    
    
    def desactivarUsuario(self, idUsuario):
        try:
            
            return  self.usuarioRepo.desactivarUsuario(idUsuario)
        except Exception as error:
            logging.error("ocurrio un error desactivando al usuario")
            logging.error(error)
            return False
        
    def obtenerUsuarioPorArea(self,idArea):
        try:
            return self.usuarioRepo.obtenerUsuariosPorArea(idArea)
        except Exception as error:
            logging.error("ocurrio un error al obtener los usuarios por id area")
            pass
    @staticmethod
    def build():
        UsuarioService._usuarioService = UsuarioService()