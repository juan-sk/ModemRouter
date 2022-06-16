class AreaUsuarioEntity:
    
    def __init__(self):
        self.idUsuario = 0
        self.idArea = 0
         
    @staticmethod    
    def creaAreaUsuarioEntity(resultSet):
        u = AreaUsuarioEntity()
        u.idUsuario  = resultSet[0]
        u.idArea  = resultSet[0]


        return u
    @staticmethod    
    def fromUsuario(usuario):
        au = AreaUsuarioEntity()
        au.idUsuario  = usuario.id
        au.idArea  = usuario.idArea
        return au