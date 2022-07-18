from gui.jefemesa.ConsultaTickets import ConsultaTickets
from gui.jefemesa.GestionarAreas import GestionarAreas
from gui.jefemesa.GestionarTiposTicket import GestionarTiposTicket
from gui.jefemesa.GestionarUsuario import GestionarUsuario
from utils.GuiInputUtils import GuiInputUtils
from utils.GuiUtils import GuiUtils


class JefeMesa:
    
    def __init__(self):
        self.gestionarUsuario =GestionarUsuario() 
        self.gestionarAreas = GestionarAreas()
        self.gestionarTiposTicket = GestionarTiposTicket()
        self.conslutaTickets = ConsultaTickets()
    
    def start(self):
        while True:
            
            opcion = self.menuOpcionesJefeMesa()
            
            if opcion == 1:
                self.gestionarUsuario.start()
            elif opcion ==2:
                self.gestionarAreas.start()
            elif opcion ==3:
                self.gestionarTiposTicket.start()
            elif opcion ==4:
                self.conslutaTickets.start()
                pass    
            elif opcion ==5:
                break
        
    def menuOpcionesJefeMesa(self):
        GuiUtils.clearTerminal()
        print( GuiUtils.subrrayar( "Opcions jefeesa"))
        print("1). Gestionar Usuarios")
        print("2). Gestionar Areas")
        print("3). Gestionar Tipos Ticket")
        print("4). Consultar Tickets")
        print("5). Cerrar Sesion")
        
        opcionesValidas = [1,2,3,4,5]
        opcion = GuiInputUtils.inputNumber(opcionesValidas)
        return opcion