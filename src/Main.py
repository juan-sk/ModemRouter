from asyncio.log import logger
import logging
from config.ComponentConfig import ComponentConfig
from config.Config import Config
from config.DBConection import DbConnection
from gui.Gui import Gui
from repository.AreaRepository import AreaRepository
from repository.CriticidadRepository import CriticidadRepository
from repository.TicketRepository import TicketRepository
from repository.TipoTicketRepository import TipoTicketRepository
from repository.UsuarioRepository import UsuarioRepository



class Application:
      
  def __init__(self):
    Config.configurar()
    ComponentConfig.createComponents()
    logging.info("########### [INICIO DE LA APLICACION] ###############")
    logging.info("configurando dependencias")
    self.trepo = TicketRepository()
    self.uRepo = UsuarioRepository() 
    self.ttRepo = TipoTicketRepository() 
    self.areaRepo = AreaRepository() 
    self.criticidadRepo = CriticidadRepository() 
        
  def start(self):
    value = 0
    logging.info("Start de aplicacion")
    logger.info("informacion")
    while True:
      self.mainEventLoop()
      value = value+1
      if(value >=1):
        break   
    self.stop()
    
    
  def mainEventLoop(self):
    gui = Gui()
    gui.gui()
         
        
        
        
  def stop(self):
    DbConnection.close()
    logging.info("########### [FIN DE LA APLICACION] ###############")
    
            
            
  
def main():
    App = Application()
    try:
        App.start()
    except Exception as error :
        print("ERROR - ocurrio un error")
        print(error)
        App.stop()  
  


if __name__ == "__main__":
    main()