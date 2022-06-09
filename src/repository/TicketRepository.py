import logging
from config.Config import Config
from entity.TicketEntity import TicketEntity


class TicketRepository:
    
    def __init__(self):
        self._dbConn = Config().DBConnection
        
    def obtenerTickets(self):
        try:
            SQL = "SELECT * FROM tma.ticket"
            cursor =  self._dbConn.cursor()
        
            cursor.execute(SQL)

            result= cursor.fetchall()
            cursor.close()  
            
            res = []
            for item in result:
                res.append(TicketEntity.creaTicketEntity(item))
            return res
        except Exception as error:
            logging.error("ocurrio un error al intentar obtener los tickets")
            logging.error(error)
            raise Exception