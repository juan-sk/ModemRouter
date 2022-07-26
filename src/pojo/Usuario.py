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
    
    def println(self):
        print("|%5d | %20s | %9s | %30s | %30s | "
              %(
                self.id,
                self.nombreUsuario,
                self.dscEstado,
                self.dscTipoUsuario,
                self.dscArea
               ))
        
    @staticmethod
    def fromUsuario(usuario, listaTiposUsuario, area):
        u = Usuario()
        u.id = usuario.id
        u.nombreUsuario = usuario.nombreUsuario
        for item in listaTiposUsuario:
            if(item.id == usuario.idTipoUsuario):
                u.idTipoUsuario = item.id
                u.dscTipoUsuario = item.nomTipoUsuario
                break
        u.idArea = area.id
        u.dscArea = area.nomArea
        u.idEstado = usuario.idEstado
        if usuario.idEstado ==1:
            u.dscEstado = "Activo"
        else:
            u.dscEstado = "Inactivo"
        return u
    
    @staticmethod
    def creaUsuario(rs):
        u = Usuario()
        u.id =int(rs[0])
        u.nombreUsuario=rs[1]
        u.password = rs[2]
        u.idEstado=int(rs[3])
        u.dscEstado = rs[4]
        u.idTipoUsuario=int(rs[5])
        u.dscTipoUsuario=rs[6]
        u.idArea = int(rs[7])
        u.dscArea = rs[8]
        return u
             
        