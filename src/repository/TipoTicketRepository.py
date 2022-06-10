import logging
from config.Config import Config
from entity.TipoTicketEntity import TipoTicketEntity


class TipoTicketRepository:
    
    def __init__(self):
        self._dbConn = Config().DBConnection
        
    def obtenerTipoTickets(self):
        try:
            SQL = "SELECT * FROM tma.tipo_ticket"
            cursor =  self._dbConn.cursor()
        
            cursor.execute(SQL)

            result= cursor.fetchall()
            cursor.close()  
            
            res = []
            for item in result:
                res.append(TipoTicketEntity.creaTipoTicketEntity(item))
            return res
        except Exception as error:
            logging.error("ocurrio un error al intentar obtener los tipos de ticket")
            logging.error(error)
            raise Exception