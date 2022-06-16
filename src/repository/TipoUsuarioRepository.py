import logging
from config.Config import Config
from entity.TipoTicketEntity import TipoTicketEntity
from entity.TipoUsuarioEntity import TipoUsuarioEntity

class TipoUsuarioRepository:
    
    def __init__(self):
        self._dbConn = Config().DBConnection
        
    def obtenerTipoUsuarios(self):
        try:
            SQL = "SELECT * FROM tma.tipo_usuario"
            cursor =  self._dbConn.cursor()
        
            cursor.execute(SQL)

            result= cursor.fetchall()
            cursor.close()  
            
            res = []
            for item in result:
                res.append(TipoUsuarioEntity.creaTipoUsuario(item))
            return res
        except Exception as error:
            logging.error("ocurrio un error al intentar obtener los tipos de usuario")
            logging.error(error)
            raise Exception