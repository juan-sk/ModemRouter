import logging
from gui.ejecutivomesa.opciones.CreaTicket import CreaTicket
from gui.ejecutivomesa.opciones.VerTickets import VerTickets
from utils.GuiUtils import GuiUtils


class EjecutivoMesa:
    
    def __init__(self):
       self.creaTicket = CreaTicket()
    
    
     
    def start(self,idUsuario):
        while True:
            opcion =    self.menuOpciones()
            
            if opcion == 1:
                print("ver Tickets")
                VerTickets().start()
            elif opcion ==2:
                print("Crear tiket")
                CreaTicket().start(idUsuario)
            elif opcion == 3:
                print("salir")
                return True

    def menuOpciones(self):
        
        while True:
            try:
                GuiUtils.clearTerminal()
                print("     Menu Ejecutivo Mesa         ")
                print("")
  
                
                print(GuiUtils.subrrayar("Opcions"))
                print("1). Ver tickets")
                print("2). Crear Ticket")
                print("3). Cerrar Secion")
                opcionesValidas  = [1,2,3]
                value = int(input("Ingrese Opcion:"))
                if value in opcionesValidas:
                    # opcionMenu = value 
                    return value 
                else: 
                    print("ingrese una opcion Valida")
            except Exception as error :
                logging.error("ocurio un error en el menu de opciones de gestion de usuario")
                logging.error(error)
                print("ocurrio un error con la opcion que ingreso")