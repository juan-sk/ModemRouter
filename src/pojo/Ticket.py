from datetime import datetime


class Ticket:
    
    def __init__(self):
        self.idTicket = 0
        self.nombreCliente = ""
        self.rutCliente = ""
        self.telefono = ""
        self.correoElectronico = ""
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
        t.correoElectronico = rs[4]
        t.detalle = rs[5]
        t.observacion =rs[6]
        t.idEstado=int(rs[7])
        t.nomEstado=rs[8]
        t.fechaCreacion  = rs[9]
        t.idUsuarioCreacion = int(rs[10])
        t.nombreUsuarioCreacion =rs[11]
        t.idUsuarioDerivado = int(rs[12])
        t.nombreUsuarioDerivado = rs[13]
        t.idCriticidad= int(rs[14])
        t.nomCriticidad = rs[15]
        t.idArea = int(rs[16])
        t.nomArea =rs[17]
        t.idTipoTicket = int(rs[18])
        t.nomTipoTicket = rs[19]
        return t
  
        
        