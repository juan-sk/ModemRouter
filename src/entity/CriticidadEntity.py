class CriticidadEntity:
    
    def __init__(self) :
        self.id =0
        self.nomCriticidad=""
        self.dscCriticidad = ""

       
    @staticmethod    
    def creaCriticidadEntity(resultSet):
        u = CriticidadEntity()
        u.id  = resultSet[0]
        u.nomCriticidad = resultSet[1]
        u.dscCriticidad = resultSet[2]

        return u
    
    def __str__(self):
        return "CriticidadEntity(id:"+str(self.id)+ ", nomCriticidad:"+str(self.nomCriticidad)+", dscCriticidad:"+str(self.dscCriticidad)+")"