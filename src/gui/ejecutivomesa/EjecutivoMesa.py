import logging
from gui.ejecutivomesa.opciones.CreaTicket import CreaTicket
from gui.ejecutivomesa.opciones.VerTickets import VerTickets
from entity.TicketEntity import TicketEntity
from utils.GuiUtils import GuiUtils


class EjecutivoMesa:
    
    def __init__(self):
       self.creaTicket = CreaTicket()
       self.VerTickets = VerTickets()   
     
    def start(self,idUsuario):
        while True:
            opcion = self.menuOpciones()
            if opcion == 1:
                #print("ver Tickets")
                VerTickets().start()
            elif opcion == 2:
                #print("Crear tiket")
                CreaTicket().start(idUsuario)
            elif opcion == 0:
                #print("salir")
                return True

    def menuOpciones(self):
        
        while True:
            try:
                GuiUtils.clearTerminal()
                GuiUtils.titulo("Ejecutivo mesa de ayuda")
                GuiUtils.subtitulo("Menu de opciones ")
                GuiUtils.izq("1) Ver tickets")
                GuiUtils.izq("2) Crear Ticket")
                GuiUtils.izq("0) Cerrar sesión")
                GuiUtils.separador()
                opcionesValidas  = [0,1,2]
                value = int(input(" Ingrese un n° de opción para continuar: "))
                if value in opcionesValidas:
                    # opcionMenu = value 
                    return value 
            except Exception as error :
                logging.error("ocurio un error en el menu de opciones de gestion de usuario")
                logging.error(error)
                print("ocurrio un error con la opcion que ingreso")