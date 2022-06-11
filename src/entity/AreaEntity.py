class AreaEntity:
    
    def __init__(self) :
        self.id =0
        self.nomArea=""
        self.dscArea = ""

       
    @staticmethod    
    def creaAreaEntity(resultSet):
        u = AreaEntity()
        u.id  = resultSet[0]
        u.nomArea = resultSet[1]
        u.dscArea = resultSet[2]

        return u
    
    def __str__(self):
        return "AreaEntity(id:"+str(self.id)+ ", nomArea:"+str(self.nomArea)+", dscArea:"+str(self.dscArea)+")"