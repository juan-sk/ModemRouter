import mysql.connector

import os

class DBConnection:

    @staticmethod
    def conectarDB():
        try:
            print("Conectando a la base de datos...")

            DBConnection._db = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USERNAME"),
            password =os.getenv("DB_PASSWORD"),
            database = os.getenv("DB_NAME")
            )
            print("Conexcion exitosa ")
            return DBConnection._db
        
        except Exception:
            raise Exception("ocurrio un error conectandose a la db")
        
    @staticmethod
    def close():
        print("Desconectando la base de Datos...")
        DBConnection._db.close()
        print("Se desconecto la Base de Datos")