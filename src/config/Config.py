from distutils.command.config import config
import logging
from config.DBConection import DBConnection
from config.Env import Env
from config.LogConfig import LogConfig

class Config:
    
    @staticmethod
    def configurar():
        # cargar variables de entorno
        print("configurando env")
        Env.configs()
        
        print("configurando Log")
        LogConfig.configurar();
        # conectar db
        logging.info("configurando db")
        Config.DBConnection = DBConnection.conectarDB()
        
    
     