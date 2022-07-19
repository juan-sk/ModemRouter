import logging
from config.Config import Config
from entity.TipoTicketEntity import TipoTicketEntity


class TipoTicketRepository:
    
    def __init__(self):
        self._dbConn = Config._dbConnection
        
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
    def obtenerCantidadTicketsRelacionados(self, idticket):
        try:
            SQL = """
            SELECT
                count(*)
            FROM
                tma.ticket as t
                join tma.tipo_ticket as tt on t.id_tipo_ticket = tt.id_tipo_ticket
            where
                tt.id_tipo_ticket = %s
                """
            cursor =  self._dbConn.cursor()
            val = (idticket,)
            cursor.execute(SQL,val)

            result= cursor.fetchall()
            cursor.close()  
            cantidad = result[0][0]
            return cantidad
        except Exception as error:
            logging.error("ocurrio un error al intentar obtener los tipos de ticket")
            logging.error(error)
            raise Exception 
    def guardar(self, tipoTicket):
        try:
            SQL = """
            INSERT INTO
                `tma`.`tipo_ticket` (
                    `nom_tipo_ticket`,
                    `dsc_tipo_ticket`
                )
            VALUES
                (
                    %s,
                    %s
                )
                """
            cursor =  self._dbConn.cursor()
            val = (tipoTicket.nomTipoTicket,tipoTicket.dscTipoTicket)
            cursor.execute(SQL,val)

            self._dbConn.commit()
            cursor.close()  

        except Exception as error:
            logging.error("ocurrio un error al intentar obtener los tipos de ticket")
            logging.error(error)
            raise Exception 
    def modificar(self,tipoTicket):
        try:
            SQL = """
            UPDATE
                `tma`.`tipo_ticket`
            SET
                `nom_tipo_ticket` = %s,
                `dsc_tipo_ticket` = %s
            WHERE
                `id_tipo_ticket` = %s
                """
            cursor =  self._dbConn.cursor()
            val = (
                tipoTicket.nomTipoTicket,
                tipoTicket.dscTipoTicket,
                tipoTicket.id
                )
            cursor.execute(SQL,val)

            self._dbConn.commit()
            cursor.close()  

        except Exception as error:
            logging.error("ocurrio un error al intentar obtener los tipos de ticket")
            logging.error(error)
            raise Exception 
        
    def eliminar(self,idTipoTicket):
        try:
            SQL = """
                DELETE FROM
                    `tma`.`tipo_ticket`
                WHERE
                  id_tipo_ticket =  %s
                """
            cursor =  self._dbConn.cursor()
            val = (
              idTipoTicket,
                )
            cursor.execute(SQL,val)

            self._dbConn.commit()
            cursor.close()  

        except Exception as error:
            logging.error("ocurrio un error al intentar obtener los tipos de ticket")
            logging.error(error)
            raise Exception 
    @staticmethod
    def build():
        TipoTicketRepository._tipoTicketRepository = TipoTicketRepository()