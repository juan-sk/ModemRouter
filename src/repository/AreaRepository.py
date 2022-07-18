import logging
from config.Config import Config
from entity.AreaEntity import AreaEntity
from entity.TicketEntity import TicketEntity


class AreaRepository:
    
    def __init__(self):
        # if AreaRepository._areaRepository != None:
        #     raise Exception("AreaRepository ya ha sido iniciado antes")
        self._dbConn = Config._dbConnection
        
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
        
    def obtenerAreaUsuaio(self,idUsuario):
        try:
            SQL = "SELECT distinct(a.id_area), nom_area, dsc_area FROM tma.area as a left join tma.area_usuario as au on a.id_area = au.id_area where au.id_usuario = %s "
            VALUES = tuple((idUsuario,))
            cursor =  self._dbConn.cursor()
        
            cursor.execute(SQL,VALUES)

            result= cursor.fetchall()
            cursor.close()  
        
            if len(result)>0:
                return AreaEntity.creaAreaEntity(result[0])
            else:
                return AreaEntity()
        except Exception as error:
            logging.error("ocurrio un error al intentar obtener las areas")
            logging.error(error)
            raise Exception
    @staticmethod
    def build():
        AreaRepository._areaRepository = AreaRepository()