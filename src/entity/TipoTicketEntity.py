class TipoTicketEntity:
    
    def __init__(self) :
        self.id =0
        self.nomTipoTicket=""
        self.dscTipoTicket = ""

       
    @staticmethod    
    def creaTipoTicketEntity(resultSet):
        u = TipoTicketEntity()
        u.id  = resultSet[0]
        u.nomTipoTicket = resultSet[1]
        u.dscTipoTicket = resultSet[2]

        return u
    
    def __str__(self):
        return "TipoTicketEntity(id:"+str(self.id)+ ", nomTipoTicket:"+str(self.nomTipoTicket)+", dscTipoTicket:"+str(self.dscTipoTicket)+")"
    
    def print(self):
        m = """
        Detalle del Tipo de Ticket
        
        Nombre Tipo Ticket:             %s
        Descripcion del Tipo de Ticket: %s
        
        """%(self.nomTipoTicket,self.dscTipoTicket)
        print(m)