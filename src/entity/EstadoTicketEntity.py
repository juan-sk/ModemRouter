class EstadoTicketEntity:
    
    
    def __init__(self):
        self.id = 0
        self.nomEstadoTicket = ""
        self.dscEstadoTicket = ""
    @staticmethod
    def creaEstadoTicket(resultSet):
        e = EstadoTicketEntity()
        e.id = resultSet[0]
        e.nomEstadoTicket = resultSet[1]
        e.dscEstadoTicket = resultSet[2]
        return e