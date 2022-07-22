from controller.EjecutivoMesaController import EjecutivoMesaController
from utils.GuiUtils import GuiUtils 
import logging

class VerTickets:
    
    def __init__(self):
        self.EjecutivoMesaController = EjecutivoMesaController._ejecutivoMesaController
        pass
    
    def start(self):
        tickets = self.EjecutivoMesaController.obtenerTickets()
        print(tickets)
        self.mostrarTickets(tickets)
        input("Presione Enter para Continuar ...")

    def mostrarTickets(self,tickets):
        GuiUtils.clearTerminal()
        print(GuiUtils.subrrayar("Tickets"))
        try:
            HEADER = "    %s     |    %s                      |    %s    |    %s    "%("ID","Creacion","Cliente","Detalle")
            print(HEADER)
            for item in tickets:
                printString  = "    %s      |    %s           |    %s  |    %s    "%(item.id,item.fechaCreacion,item.nombreCliente,item.detalle)
                print (printString)
                
        except Exception as error:
            logging.error("ocurrio un error al mostrar los tickets")
            logging.error(error)