import logging
from config.Config import Config
from entity.EstadoTicketEntity import EstadoTicketEntity


class EstadoTicketRepository:
    
    def __init__(self):
        self._dbConn = Config().DBConnection
    
    def obtenerEstadosTicket(self):
        try:
            SQL = "SELECT * FROM tma.estado_ticket"
            cursor =  self._dbConn.cursor()
        
            cursor.execute(SQL)

            result= cursor.fetchall()
            cursor.close()  
            
            res = []
            for item in result:
                res.append(EstadoTicketEntity.creaTicketEntity(item))
            return res
        except Exception as error:
            logging.error("ocurrio un error al intentar obtener los estados del ticket")
            logging.error(error)
            raise Exception