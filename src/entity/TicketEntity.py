from datetime import datetime


class TicketEntity:
    
    def __init__(self) :
        self.id =0
        self.nombreCliente=""
        self.rutCliente=""
        self.telefono=""
        self.detalle=""
        self.observacion=""
        self.idEstado=0
        self.fechaCreacion = datetime.now()
        self.idUsuarioCreacion = 0
        self.idUsuarioDerivado = 0
        self.idCriticidad = 0
        self.idArea = 0
        self.idTipoTicket = 0
    @staticmethod    
    def creaTicketEntity(resultSet):
        t = TicketEntity()
        t.id  = resultSet[0]
        t.nombreCliente = resultSet[1]
        t.rutCliente = resultSet[2]
        t.telefono = resultSet[3]
        t.detalle = resultSet[4]
        t.observacion = resultSet[5]
        t.estado = resultSet[6]
        t.fechaCreacion = resultSet[7]
        t.idUsuarioCreacion = resultSet[8]
        t.idUsuarioDerivado = resultSet[9]
        t.idCriticidad = resultSet[10]
        t.idArea = resultSet[11]
        t.idTipoTicket = resultSet[12]
        return t
    def fromTicket(tt):
        t = TicketEntity()
        t.id  = tt.idTicket
        t.nombreCliente = tt.nombreCliente
        t.rutCliente = tt.rutCliente
        t.telefono = tt.telefono
        t.detalle = tt.detalle
        t.observacion = tt.observacion
        t.idEstado = tt.idEstado
        t.fechaCreacion = tt.fechaCreacion
        t.idUsuarioCreacion = tt.idUsuarioCreacion
        t.idUsuarioDerivado = tt.idUsuarioDerivado
        t.idCriticidad = tt.idCriticidad
        t.idArea = tt.idArea
        t.idTipoTicket = tt.idTipoTicket
        return t
    
    def __str__(self):
        return "TicketEntity(id:"+str(self.id)+", nombreCliente:"+str(self.nombreCliente)+", rutCliente:"+self.rutCliente