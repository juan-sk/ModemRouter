from asyncio.log import logger
import logging
from config.Config import Config
from config.DBConection import DBConnection
from repository.TicketRepository import TicketRepository
from repository.TipoTicketRepository import TipoTicketRepository
from repository.UsuarioRepository import UsuarioRepository



class Application:
      
  def __init__(self):
    Config().configurar()
    logging.info("########### [INICIO DE LA APLICACION] ###############")
    logging.info("configurando dependencias")
    self.trepo = TicketRepository()
    self.uRepo = UsuarioRepository() 
    self.ttRepo = TipoTicketRepository() 
        
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
    #login        
    # todo el codigo deberia ir aqui
    # tickets = self.trepo.obtenerTickets()
    # for item in tickets:
    #   print (item)
    # usuarios = self.uRepo.obtenerUsuarios()
    # for item in usuarios:
    #   print (item)
    tipoTicket = self.ttRepo.obtenerTipoTickets()
    for item in tipoTicket:
      print (item)
         
        
        
        
  def stop(self):
    DBConnection.close()
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