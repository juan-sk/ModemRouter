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
        
        
        
    def guardarTicket(self,ticket):
        try:
            cursor =  self._dbConn.cursor()
            SQL = """
            INSERT INTO
                `tma`.`ticket` (
                    `id_ticket`,
                    `nombre_cliente`,
                    `rut_cliente`,
                    `telefono`,
                    `detalle`,
                    `observacion`,
                    `id_estado`,
                    `fecha_creacion`,
                    `id_usuario_creacion`,
                    `id_usuario_derivado`,
                    `id_criticidad`,
                    `id_area`,
                    `id_tipo_ticket`
                )
            VALUES
                (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                );

            """
            val = (
                ticket.idTicket,
                ticket.nombreCliente,
                ticket.rutCliente,
                ticket.telefono,
                ticket.detalle,
                ticket.observacion,
                ticket.idEstado,
                ticket.fechaCreacion,
                ticket.idUsuarioCreacion,
                ticket.idUsuarioDerivado,
                ticket.idCriticidad,
                ticket.idArea,
                ticket.idTipoTicket,
               
            )
            cursor.execute(SQL, val)
        except Exception as error:
            logging.error("ocurrio un error al guardar el ticket en la base de datos")
            logging.error(error)
        