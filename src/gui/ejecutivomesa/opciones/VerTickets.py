from controller.EjecutivoMesaController import EjecutivoMesaController
from utils.GuiUtils import GuiUtils 
import logging

class VerTickets:
    
    def __init__(self):
        self.EjecutivoMesaController = EjecutivoMesaController._ejecutivoMesaController
        pass
    
    def start(self):
        tickets = self.EjecutivoMesaController.obtenerTickets()
        self.mostrarTickets(tickets)

    def mostrarTickets(self,tickets):
        GuiUtils.clearTerminal()
        GuiUtils.titulo("Ejecutivo mesa de ayuda")
        GuiUtils.subtitulo(" Listado de tickets generados")        
        try:
            #HEADER = "    %s     |    %s                      |    %s    |    %s    "%("ID","Creacion","Cliente","Detalle")
            GuiUtils.espaciado()
            header = "|" + GuiUtils.customText(2, 9, " ", "ID")
            header += "|" + GuiUtils.customText(2, 24, " ", "Creación")
            header += "|" + GuiUtils.customText(2, 63, " ", "Cliente") + "|"
            print(header)
            GuiUtils.espaciado()
            print("| " + GuiUtils.customText( 1, 97, " ", "Detalle") + "|")
            GuiUtils.espaciado()
            GuiUtils.separador()
            for item in tickets:
                #printString  = "    %s      |    %s           |    %s  |    %s    "%(item.id,item.fechaCreacion,item.nombreCliente,item.detalle)
                GuiUtils.espaciado()
                data = "|" + GuiUtils.customText(2, 9, " ", item.id)
                data += "|" + GuiUtils.customText(2, 24, " ", item.fechaCreacion)
                data += "|" + GuiUtils.customText(2, 63, " ", item.nombreCliente) + "|"
                print(data)
                GuiUtils.espaciado()
                print("| " + GuiUtils.customText( 1, 97, " ", item.detalle) + "|")
                GuiUtils.espaciado()
                GuiUtils.separador()       
            input(" Presione cualquier tecla continuar...")
        except Exception as error:
            logging.error("ocurrio un error al mostrar los tickets")
            logging.error(error)