import logging
from config.Config import Config
from entity.EstadoUsuarioEntity import EstadoUsuarioEntity


class EstadoUsuarioRepository:
    
    def __init__(self):
        self._dbConn = Config().DBConnection
    
    def obtenerEstadosUsuario(self):
        try:
            SQL = "SELECT * FROM tma.estado_usuario"
            cursor =  self._dbConn.cursor()
        
            cursor.execute(SQL)

            result= cursor.fetchall()
            cursor.close()  
            
            res = []
            for item in result:
                res.append(EstadoUsuarioEntity.creaAreaUsuarioEntity(item))
            return res
        except Exception as error:
            logging.error("ocurrio un error al intentar obtener los estados de usuario")
            logging.error(error)
            raise Exception