class EstadoUsuarioEntity:
    
    def __init__(self):
        self.id = 0
        self.nomEstado =""
        self.dscEstado = ""
        
    @staticmethod
    def creaEstadoTicket(resultSet):
        e = EstadoUsuarioEntity()
        e.id = resultSet[0]
        e.nomEstado = resultSet[1]
        e.dscEstado = resultSet[2]
        return e