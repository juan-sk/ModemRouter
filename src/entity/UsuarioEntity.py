from types import NoneType


class UsuarioEntity:
    
    def __init__(self) :
        self.id =0
        self.nombreUsuario=""
        self.password = ""
        self.idEstado=0
        self.idTipoUsuario=0
       
    @staticmethod    
    def creaUsuarioEntity(resultSet):
        u = UsuarioEntity()
        if resultSet !=None:
            u.id  = resultSet[0]
            u.nombreUsuario = resultSet[1]
            u.password = resultSet[2]
            u.idEstado = resultSet[3]
            u.idTipoUsuario = resultSet[4]
        return u
    @staticmethod
    def fromUsuario(usuario):
        u = UsuarioEntity()
        u.id = usuario.id
        u.nombreUsuario =usuario.nombreUsuario
        u.password = usuario.password
        u.idEstado = usuario.idEstado
        u.idTipoUsuario = usuario.idTipoUsuario
        return u
    

    def __str__(self):
        return "UsuarioEntity(id:"+str(self.id)+ ", nombreUsuario:"+str(self.nombreUsuario)+", password:"+str(self.password)+", idEstado:"+str(self.idEstado)+", idTipoUsuario:"+str(self.idTipoUsuario)+")"