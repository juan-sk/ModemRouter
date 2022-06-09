from asyncio.log import logger
import logging
import os


class LogConfig:
    @staticmethod
    def configurar():
        logPath = os.getenv("LOG_FILE_PATH")
        logFileName = "mesaAyuda.log"
        full = logPath +logFileName
        logging.basicConfig(filename=full, filemode='a', format='%(asctime)s - %(levelname)s [%(name)s] %(message)s',level=os.getenv("LOG_LEVEL"))
        logging.info("log configurado correctamente")


    
