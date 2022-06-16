class Usuario:
    
    def __init__(self):
        self.id =0
        self.nombreUsuario=""
        self.password = ""
        self.idEstado=0
        self.idTipoUsuario=0
        self.idArea = 0
        
    def __str__(self):
        return "Usuario(id:"+str(self.id)+ ", nombreUsuario:"+str(self.nombreUsuario)+", password:"+str(self.password)+", idEstado:"+str(self.idEstado)+", idTipoUsuario:"+str(self.idTipoUsuario)+", idArea:"+str(self.idArea)+")"