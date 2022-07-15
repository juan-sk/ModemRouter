from datetime import datetime


class Ticket:
    
    def __init__(self):
        self.idTicket = 0
        self.nombreCliente = ""
        self.rutCliente = ""
        self.telefono = ""
        self.detalle = ""
        self.observacion =""
        self.idEstado=0
        self.nomEstado=""
        self.fechaCreacion  = datetime.now()
        self.idUsuarioCreacion =0
        self.nombreUsuarioCreacion =""
        self.idUsuarioDerivado = 0
        self.nombreUsuarioDerivado = ""
        self.idCriticidad=0
        self.nomCriticidad = ""
        self.idArea = 0
        self.nomArea =""
        self.idTipoTicket = 0
        self.nomTipoTicket = ""
        
        