import logging
from controller.JefeDeMesaController import JefeDeMesaController
from entity.AreaEntity import AreaEntity
from utils.GuiInputUtils import GuiInputUtils
from utils.GuiUtils import GuiUtils


class GestionarAreas:
    
    def __init__(self):
        self.jefeDeMesaController = JefeDeMesaController._jefeDeMesaController 
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
        while True:
            print(" Crear Area ")
            area = AreaEntity()
            area.nomArea= input("Ingrese Nombre Area: ")
            area.dscArea = input("Ingrese descripcion del Area: ")
            area.print()
            input("Presione Enter para continuar Con el Guardado del Area")
            # guardar area 
            try:
                self.jefeDeMesaController.guardarArea(area)
                print("Se guardo Correctamente el area")
                input("Presione Enter para Continuar ")
                break
            except Exception as error :
                logging.error("ocurrion un error guardando el area")
                logging.error(error)
                print("ocurrio un error en el guardado del Area")
                print("Desea intentar nuevamente? (SI/NO)")
                respuesta = GuiInputUtils.inputSiNo()
                if respuesta ==1:
                    continue
                else:
                    # salir del bucle 
                    break
       
    
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