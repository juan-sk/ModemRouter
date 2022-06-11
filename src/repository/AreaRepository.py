import logging
from config.Config import Config
from entity.AreaEntity import AreaEntity
from entity.TicketEntity import TicketEntity


class AreaRepository:
    
    def __init__(self):
        self._dbConn = Config().DBConnection
        
    def obtenerAreas(self):
        try:
            SQL = "SELECT * FROM tma.area"
            cursor =  self._dbConn.cursor()
        
            cursor.execute(SQL)

            result= cursor.fetchall()
            cursor.close()  
            
            res = []
            for item in result:
                res.append(AreaEntity.creaAreaEntity(item))
            return res
        except Exception as error:
            logging.error("ocurrio un error al intentar obtener las areas")
            logging.error(error)
            raise Exception