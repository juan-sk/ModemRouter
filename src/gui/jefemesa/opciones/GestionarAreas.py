from utils.GuiInputUtils import GuiInputUtils
from utils.GuiUtils import GuiUtils


class GestionarAreas:
    
    def __init__(self):
        pass
    
    def start(self):
        
        while True:
            
            GuiUtils.clearTerminal()
            
            opcion = self.menuOpciones()
            if opcion == 1:
                self.crearArea()
            elif opcion ==2:
                self.modificarArea()
            elif opcion ==3:
                pass
            elif opcion ==4:
                break
    
    def crearArea(self):
        print(" Crear Area ")
        input()
    
    def modificarArea(self):
        
        pass
    
    def eliminarAreas(self):
        pass
    def mostrarAreas(self,areas):
        pass
    def menuOpciones(self):
        
        print(GuiUtils.subrrayar(" Opciones ")) 
        print("")            
        print("1). Crear Area")            
        print("2). Modificar Areas")            
        print("3). Eliminar Area")            
        print("4). Atras")            
        print("")            
        opcionsValidas = [1,2,3,4]
        return GuiInputUtils.inputNumber(opcionsValidas)