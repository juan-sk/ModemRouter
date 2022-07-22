import logging
from controller.JefeDeMesaController import JefeDeMesaController
from entity.AreaEntity import AreaEntity
from gui.OpcioensComunes import OpcionesComunes
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
                self.eliminarAreas()
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
        areas =   self.jefeDeMesaController.obtenerAreas()
        
        self.mostrarAreas(areas)
        
        opcionesValidas = []
        for item in areas:
            opcionesValidas.append(item.id)
        opcionSalida = 0
        opcionesValidas.append(opcionSalida)
        print("Ingrese el id del Area a Eliminar (ingrese 0 para salir)")
        idAreaEliminar =GuiInputUtils.inputNumber(opcionesValidas)
        
            
            
        eliminable = self.jefeDeMesaController.validarRelacionArea(idAreaEliminar)
        if eliminable:
            self.jefeDeMesaController.eliminarArea(idAreaEliminar)
        else:
            print("No se puede Eliminar el registro ya que cuenta tickets asignados")
        OpcionesComunes.presioneEnterContinuar()

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