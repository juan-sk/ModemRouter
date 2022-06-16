from gui.jefemesa.GestionarUsuario import GestionarUsuario


class JefeMesa:
    
    def __init__(self):
        self.gestionarUsuario =GestionarUsuario() 
    
    
    def start(self):
        
        self.gestionarUsuario.gestionarUsuario()
    def menuOpcionesJefeMesa(self):
        print("Opcions jefeesa")