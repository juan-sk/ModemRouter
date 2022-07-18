import logging
from config.Config import Config
from entity.AreaUsuarioEntity import AreaUsuarioEntity


class AreaUsuarioReposotory:
    
    def __init__(self):
        self._dbConn = Config._dbConnection
        
    def obtenerAreasUsuarios(self):
        try:
            SQL = "SELECT * FROM tma.area"
            cursor =  self._dbConn.cursor()
        
            cursor.execute(SQL)

            result= cursor.fetchall()
            cursor.close()  
            
            res = []
            for item in result:
                res.append(AreaUsuarioEntity.creaAreaUsuarioEntity(item))
            return res
        except Exception as error:
            logging.error("ocurrio un error al intentar obtener las areas")
            logging.error(error)
            raise Exception
        
    def guardarAreaUsuario(self,cursor,areaUsuario):
        SQL = """
            INSERT INTO
                `tma`.`area_usuario` (`id_usuario`, `id_area`)
            VALUES
                (%s,%s);
        """

        val = (
            areaUsuario.idUsuario,
            areaUsuario.idArea
        )
        cursor.execute(SQL, val)   
    @staticmethod
    def build():
        AreaUsuarioReposotory._areaUsuarioReposotory = AreaUsuarioReposotory()
