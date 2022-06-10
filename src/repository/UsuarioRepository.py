import logging
from config.Config import Config
from entity.TicketEntity import TicketEntity
from entity.UsuarioEntity import UsuarioEntity


class UsuarioRepository:
    
    def __init__(self):
        self._dbConn = Config().DBConnection
        
    def obtenerUsuarios(self):
        try:
            SQL = "SELECT * FROM tma.usuario"
            cursor =  self._dbConn.cursor()
        
            cursor.execute(SQL)

            result= cursor.fetchall()
            cursor.close()  
            
            res = []
            for item in result:
                res.append(UsuarioEntity.creaUsuarioEntity(item))
            return res
        except Exception as error:
            logging.error("ocurrio un error al intentar obtener los usuarios")
            logging.error(error)
            raise Exception