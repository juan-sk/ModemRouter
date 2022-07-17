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
    @staticmethod    
    def creaTicket(rs):
        t = Ticket()
        t.idTicket = int(rs[0])
        t.nombreCliente = rs[1]
        t.rutCliente = rs[2]
        t.telefono = rs[3]
        t.detalle = rs[4]
        t.observacion =rs[5]
        t.idEstado=int(rs[6])
        t.nomEstado=rs[7]
        t.fechaCreacion  = rs[8]
        t.idUsuarioCreacion = int(rs[9])
        t.nombreUsuarioCreacion =rs[10]
        t.idUsuarioDerivado = int(rs[11])
        t.nombreUsuarioDerivado = rs[12]
        t.idCriticidad= int(rs[13])
        t.nomCriticidad = rs[14]
        t.idArea = int(rs[15])
        t.nomArea =rs[16]
        t.idTipoTicket = int(rs[17])
        t.nomTipoTicket = rs[18]
        return t
  
        
        