from gui.ejecutivomesa.CreaTicket import CreaTicket
from utils.GuiUtils import GuiUtils


class EjecutiviMesa:
    
    def __init__(self):
       self.creaTicket = CreaTicket()
    
    
     
    def start(self):
        # opciones
        self.menuOpciones()
        # self.creaTicket.start()
    def menuOpciones(self):
        print(GuiUtils.subrrayar("Opcions"))
        print("1). Ver tickets")
        print("2). Crear Ticket")
        
        MSG = """
        hola
        como 
        estas
        """
        print(MSG)