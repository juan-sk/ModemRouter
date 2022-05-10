from distutils.command.config import config
from config.DBConection import DBConnection
from config.Env import Env

class Config:
    
    @staticmethod
    def configurar():
        # cargar variables de entorno
        print("configurando env")
        Env.configs()
        # conectar db
        print("configurando db")
        Config.DBConnection = DBConnection.conectarDB()
        
    
     