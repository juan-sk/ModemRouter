from datetime import datetime


class TicketEntity:
    
    def __init__(self) :
        self.id =0
        self.nombreCliente=""
        self.rutCliente=""
        self.telefono=""
        self.correoElectronico = ""
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
        t.correoElectronico=resultSet[4]
        t.detalle = resultSet[5]
        t.observacion = resultSet[6]
        t.idEstado = resultSet[7]
        t.fechaCreacion = resultSet[8]
        t.idUsuarioCreacion = resultSet[9]
        t.idUsuarioDerivado = resultSet[10]
        t.idCriticidad = resultSet[11]
        t.idArea = resultSet[12]
        t.idTipoTicket = resultSet[13]
        return t
    def fromTicket(tt):
        t = TicketEntity()
        t.id  = tt.idTicket
        t.nombreCliente = tt.nombreCliente
        t.rutCliente = tt.rutCliente
        t.telefono = tt.telefono
        t.correoElectronico = tt.correoElectronico
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