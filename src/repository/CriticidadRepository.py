import logging
from config.Config import Config
from entity.AreaEntity import AreaEntity
from entity.CriticidadEntity import CriticidadEntity
from entity.TicketEntity import TicketEntity


class CriticidadRepository:
    
    def __init__(self):
        self._dbConn = Config().DBConnection
        
    def obtenerCriticidades(self):
        try:
            SQL = "SELECT * FROM tma.criticidad"
            cursor =  self._dbConn.cursor()
        
            cursor.execute(SQL)

            result= cursor.fetchall()
            cursor.close()  
            
            res = []
            for item in result:
                res.append(CriticidadEntity.creaCriticidadEntity(item))
            return res
        except Exception as error:
            logging.error("ocurrio un error al intentar obtener las criticidades")
            logging.error(error)
            raise Exception
    @staticmethod
    def build():
        CriticidadRepository._criticidadRepository = CriticidadRepository()