import logging
from config.Config import Config
from entity.UsuarioEntity import UsuarioEntity
from pojo.Usuario import Usuario


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
        
    def obtenerEjecutivosMesa(self):
        try:
            SQL = """
            select
                u.id_usuario,
                u.nombre_usuario,
                u.password, 
                u.id_estado, 
                eu.nom_estado,
                u.id_tipo_usuario,
                tu.nom_tipo_usuario,
                ar.id_area,
                ar.nom_area
            from
                usuario as u
                join tipo_usuario as tu on u.id_tipo_usuario = tu.id_tipo_usuario
                join estado_usuario as eu on u.id_estado = eu.id_estado
                join (
                    select
                        a.id_area,
                        au.id_usuario,
                        a.nom_area
                    from
                        area_usuario as au
                        join area as a on au.id_area = a.id_area
                ) as ar on u.id_usuario = ar.id_usuario
                    where u.id_tipo_usuario=2
            """
            cursor =  self._dbConn.cursor()
        
            cursor.execute(SQL)

            result= cursor.fetchall()
            cursor.close()  
            
            res = []
            for item in result:
                res.append(Usuario.creaUsuario(item))
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
                logging.error("no se encontro el usuario")
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
        
        
    def desactivarUsuario(self,usuario):
        
        cursor =  self._dbConn.cursor()
        db = self._dbConn
        status = 2
        if(usuario.idEstado == 2):
            status = 1
        SQL = "update usuario set id_estado = %s where id_usuario = %s"
        val = (status, usuario.id, )
        cursor.execute(SQL, val)
        

        cursor.close()  

        db.commit()
        salida = "activado"
        if(status == 2):
            salida = "desactivado"
        return salida
    
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
    def obtenerUsuario(self):
        try:
            SQL ="""
            select
                u.id_usuario,
                u.nombre_usuario,
                u.password,
                u.id_estado,
                u.id_tipo_usuario,
                tu.nom_tipo_usuario,
                eu.nom_estado,
                ar.id_area,
                ar.nom_area
            from
                usuario as u
                join tipo_usuario as tu on u.id_tipo_usuario = tu.id_tipo_usuario
                join estado_usuario as eu on u.id_estado = eu.id_estado
                join (
                    select
                        a.id_area,
                        au.id_usuario,
                        a.nom_area
                    from
                        area_usuario as au
                        join area as a on au.id_area = a.id_area
                ) as ar on u.id_usuario = ar.id_usuario
            """
            cursor =  self._dbConn.cursor()
        
            cursor.execute(SQL)

            result= cursor.fetchall()
            cursor.close()  
            
            res = []
            for item in result:
                res.append(Usuario.creaUsuarioEntity(item))
            return res
        except Exception as error:
            logging.error("ocurrio un error al intentar obtener los usuarios")
            logging.error(error)
            raise Exception

    def nombreUsuarioDisponible(self, nombreUsuario):
        try:
            SQL = "SELECT count(*) FROM usuario where  nombre_usuario = %s"
            cursor =  self._dbConn.cursor()
            val = (nombreUsuario,)
            cursor.execute(SQL,val)
            result = cursor.fetchall()
            cursor.close()  
            return result[0][0] <= 0
        except Exception as error:
            logging.error("ocurrio un error al intentar obtener los tipos de ticket")
            logging.error(error)
            raise Exception 

    def modificarUsuario(self, usuario):
        try:
            SQL = "update usuario set password = %s where id_usuario = %s"
            VALUES = (usuario.password, usuario.id, )
            cursor =  self._dbConn.cursor()
            cursor.execute(SQL,VALUES)
            result= cursor.fetchall()
            self._dbConn.commit()
            cursor.close()  
            return result
        except Exception as error:
            logging.error("ocurrio un error al intentar modificar el area")
            logging.error(error)
            raise Exception

    @staticmethod
    def build():
        UsuarioRepository._usuarioRepository = UsuarioRepository()    

        
       