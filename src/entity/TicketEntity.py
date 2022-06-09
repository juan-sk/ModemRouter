class TicketEntity:
    
    def __init__(self) :
        self.id =0
        self.nombreCliente=""
        self.rutCliente=""
        self.telefono=""
        self.detalle=""
        self.observacion=""
        self.estado=0
    @staticmethod    
    def creaTicketEntity(algo):
        t = TicketEntity()
        t.id  = algo[0]
        t.nombreCliente = algo[1]
        t.rutCliente = algo[2]
        return t
    
    def __str__(self):
        return "TicketEntity(id:"+str(self.id)+", nombreCliente:"+str(self.nombreCliente)