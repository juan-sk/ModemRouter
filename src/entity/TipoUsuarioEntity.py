class TipoUsuarioEntity:
    
    
    def __init__(self):
        self.id =0
        self.nomTipoUsuario =""
        self.dscTipoUsuraio = ""
    
    @staticmethod    
    def creaTipoUsuario(resultSet):
        u = TipoUsuarioEntity()
        u.id  = resultSet[0]
        u.nomTipoUsuario = resultSet[1]
        u.dscTipoUsuraio = resultSet[2]

        return u
    
    def __str__(self):
        return "TipoUsuario(id:"+str(self.id)+ ", nomTipoUsuario:"+str(self.nomTipoUsuario)+", dscTipoUsuraio:"+str(self.dscTipoUsuraio)+")"