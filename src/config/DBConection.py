import logging
import mysql.connector

import os

class DBConnection:

    @staticmethod
    def conectarDB():
        try:
            logging.info("Conectando a la base de datos...")
            
            DBConnection._db = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USERNAME"),
            password =os.getenv("DB_PASSWORD"),
            database = os.getenv("DB_NAME")
            )
            logging.info("Conexcion exitosa ")
            return DBConnection._db
        
        except Exception as error:
            logging.error("ocurrio un error al conectarse a la db")
            logging.error(error)
            raise Exception("ocurrio un error conectandose a la db")
        
    @staticmethod
    def close():
        try:
            logging.info("Desconectando la base de Datos...")
            DBConnection._db.close()
            logging.info("Se desconecto la Base de Datos")
        except Exception as error:
            logging.error("ocurrio un error al desconectarse de  db")
            logging.error(error)
            raise Exception("ocurrio un error desconectandose de la db")
