class Usuario:
    
    def __init__(self):
        self.id =0
        self.nombreUsuario=""
        self.password = ""
        self.idEstado=0
        self.dscEstado = "Activo"
        self.idTipoUsuario=0
        self.dscTipoUsuario=""
        self.idArea = 0
        self.dscArea = ""
        
    def __str__(self):
        return "Usuario(id:"+str(self.id)+ ", nombreUsuario:"+str(self.nombreUsuario)+", password:"+str(self.password)+", idEstado:"+str(self.idEstado)+", idTipoUsuario:"+str(self.idTipoUsuario)+", idArea:"+str(self.idArea)+")"
   
    @staticmethod
    def encontrarTipoUsuario(id,lista):
        for item in lista:
            if item.id == id:
                return item
        return None
    
    
    def print(self):
        MSG="""
     __________________________
    |    Datos de Usuario      |
    |__________________________|
    
    Nombre:      %s
    Password:    %s
    Estado:      %s
    Tipo Usuario:%s
    Area:        %s
    
            """
        print(MSG%(self.nombreUsuario,self.password,self.dscEstado,self.dscTipoUsuario,self.dscArea))