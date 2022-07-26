from gui.jefemesa.opciones.ConsultaTickets import ConsultaTickets
from gui.jefemesa.opciones.GestionarAreas import GestionarAreas
from gui.jefemesa.opciones.GestionarTiposTicket import GestionarTiposTicket
from gui.jefemesa.opciones.GestionarUsuario import GestionarUsuario
from utils.GuiInputUtils import GuiInputUtils
from utils.GuiUtils import GuiUtils


class JefeMesa:
    
    def __init__(self):
        self.gestionarUsuario =GestionarUsuario() 
        self.gestionarAreas = GestionarAreas()
        self.gestionarTiposTicket = GestionarTiposTicket()
        self.consultaTickets = ConsultaTickets()
    
    def start(self):
        while True:
            
            opcion = self.menuOpcionesJefeMesa()
            
            if opcion == 1:
                self.gestionarUsuario.start()
            elif opcion == 2:
                self.gestionarAreas.start()
            elif opcion == 3:
                self.gestionarTiposTicket.start()
            elif opcion == 4:
                self.consultaTickets.start()
                pass    
            elif opcion == 0:
                break
        
    def menuOpcionesJefeMesa(self):
        GuiUtils.clearTerminal()
        GuiUtils.titulo("Jefe de mesa de ayuda")
        GuiUtils.subtitulo("Menu de opciones ")
        GuiUtils.izq("1) Gestionar Usuarios")
        GuiUtils.izq("2) Gestionar Areas")
        GuiUtils.izq("3) Gestionar Tipos Ticket")
        GuiUtils.izq("4) Consultar Tickets")
        GuiUtils.izq("0) Cerrar sesión")
        GuiUtils.separador()
        opcionesValidas = [0,1,2,3,4]
        value = int(input(" Ingrese un n° de opción para continuar: "))
        if value in opcionesValidas:
            return value 