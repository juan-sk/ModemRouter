import logging
from config.Config import Config
from entity.UsuarioEntity import UsuarioEntity


class UsuarioRepository:
    
    def __init__(self):
        self._dbConn = Config._dbConnection
        
    def obtenerUsuarios(self):
        try:
            SQL = "SELECT * FROM tma.usuario"
            cursor =  self._dbConn.cursor()
        
            cursor.execute(SQL)

            result= cursor.fetchall()
            cursor.close()  
            
            res = []
            for item in result:
                res.append(UsuarioEntity.creaUsuarioEntity(item))
            return res
        except Exception as error:
            logging.error("ocurrio un error al intentar obtener los usuarios")
            logging.error(error)
            raise Exception
        
    def obtenerUsuarioByUsuarioAndPass(self, user, password):
        try:
            logging.info("consultando usuario")
            SQL = """SELECT * FROM tma.usuario where nombre_usuario =%s and password =%s and id_estado = 1"""
            cursor =  self._dbConn.cursor()
            data = (user,password)
            cursor.execute(SQL,data)

            result= cursor.fetchall()
            cursor.close()  
            cantidadUsuariosEncontrados = len(result)
            logging.info("se encontraron %s" %str(cantidadUsuariosEncontrados)+" usuarios")
            if(cantidadUsuariosEncontrados>0):
            
                usuario = UsuarioEntity.creaUsuarioEntity(result[0])
                return usuario
            else:
                raise Exception("no se encontro el usuario")
        except Exception as error:
            logging.error("ocurrio un error al intentar obtener los usuarios")
            logging.error(error)
            raise Exception
        
    def guardarUsuario(self,cursor, usuario):
        SQL = """
        INSERT INTO
            `tma`.`usuario` (
                `id_usuario`,
                `nombre_usuario`,
                `password`,
                `id_estado`,
                `id_tipo_usuario`
            )
        VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s
            );

        """
        val = (
            usuario.id,
            usuario.nombreUsuario,
            usuario.password,
            usuario.idEstado,
            usuario.idTipoUsuario
        )
        cursor.execute(SQL, val)
        
        
    def desactivarUsuario(self,idUsuario ):
        
        cursor =  self._dbConn.cursor()
        db = self._dbConn
        SQL = """
         update tma.usuario set id_estado = 2 where id_usuario = %s
        """
        val = (
            idUsuario,
           
        )
        cursor.execute(SQL, val)
        

        cursor.close()  

        db.commit()
        return True
    
    def obtenerUsuariosPorArea (self,idArea):
        try:
            SQL = """
            SELECT
                    u.*
                FROM
                    tma.usuario as u
                    join area_usuario as au on u.id_usuario = au.id_usuario
                where
                    u.id_estado = 1
                    and au.id_area = %s
            """
            cursor =  self._dbConn.cursor()
        
            val = (
                idArea,
            )
            cursor.execute(SQL,val)

            result= cursor.fetchall()
            cursor.close()  
            
            res = []
            for item in result:
                res.append(UsuarioEntity.creaUsuarioEntity(item))
            return res
        except Exception as error:
            logging.error("ocurrio un error al intentar obtener los usuarios")
            logging.error(error)
            raise Exception
    @staticmethod
    def build():
        UsuarioRepository._usuarioRepository = UsuarioRepository()    

        
       