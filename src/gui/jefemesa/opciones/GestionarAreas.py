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
            #elif opcion ==2:
            #    self.modificarArea()
            elif opcion == 2:
                self.eliminarAreas()
                pass
            elif opcion == 3:
                break
    
    def crearArea(self):
        while True:
            GuiUtils.clearTerminal()
            print(GuiUtils.subrrayar("Crear Area"))
            area = AreaEntity()
            area.nomArea= input("Nombre: ")
            area.dscArea = input("Descripcion: ")
            area.print()
            print()
            input("Resumen de los datos ingresados, presione una tecla para continuar...")
            # guardar area 
            try:
                self.jefeDeMesaController.guardarArea(area)
                print("Area creada, presione una tecla para continuar ")
                break
            except Exception as error :
                logging.error("ocurrion un error guardando el area")
                logging.error(error)
                print("ocurrio un error en el guardado del Area")
                print("Desea intentar nuevamente? (SI/NO)")
                respuesta = GuiInputUtils.inputSiNo()
                if respuesta == 1:
                    continue
                else:
                    # salir del bucle 
                    break
             
    def modificarArea(self):
        
        pass
    
    def eliminarAreas(self):
        while True:
            areas = self.jefeDeMesaController.obtenerAreas()
            
            self.mostrarAreas(areas)
            
            opcionesValidas = []
            for item in areas:
                opcionesValidas.append(item.id)

            opcionSalida = 0
            opcionesValidas.append(opcionSalida)

            print("Ingrese el id del Area a Eliminar (ingrese 0 para salir)")
            idAreaEliminar = GuiInputUtils.inputNumber(opcionesValidas)
            
            if idAreaEliminar == 0:
                break
            else:    
                eliminable = self.jefeDeMesaController.validarRelacionArea(idAreaEliminar)
                if eliminable:
                    print("Se inicia la eliminacion del area")
                    self.jefeDeMesaController.eliminarArea(idAreaEliminar)
                    print("Se elimino el area correctamente")
                else:
                    print("No se puede Eliminar el registro ya que cuenta tickets asignados")
                OpcionesComunes.presioneEnterContinuar()

    def mostrarAreas(self,areas):
        GuiUtils.clearTerminal()
        print(GuiUtils.subrrayar("Listado de areas"))
        HEADER = "|  ID  |    Nombre   |  Descripcion   |"
        print(HEADER)        
        for item in areas:
            print("| %3s  | %30s | %30s |"%(item.id, item.nomArea, item.dscArea))

    def menuOpciones(self):
        
        print(GuiUtils.subrrayar("Gestionar area")) 
        print()            
        print("1). Crear Area")            
        #print("2). Modificar Areas")            
        print("2). Eliminar Area")            
        print("3). Atras")            
        print()            
        opcionsValidas = [1,2,3]
        return GuiInputUtils.inputNumber(opcionsValidas)