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
            
            opcion = self.menuOpciones()

            if opcion == 1:
                self.crearArea()
            elif opcion == 2:
                self.modificarArea()
            elif opcion == 3:
                self.eliminarAreas()
                pass
            elif opcion == 0:
                break
    
    def crearArea(self):
        while True:
            GuiUtils.clearTerminal()
            GuiUtils.titulo("Jefe de mesa de ayuda")
            GuiUtils.subtitulo(" Creación de área")
            GuiUtils.subtitulo(" Por favor ingrese el detalle requerido: ")
            area = AreaEntity()
            area.nomArea= input(" Nombre: ")
            area.dscArea = input(" Descripción: ")
            # guardar area 
            try:
                self.jefeDeMesaController.guardarArea(area)
                GuiUtils.clearTerminal()
                GuiUtils.tituloEspaciado("Área creada correctamente")
                input(" Presione cualquier tecla continuar...")
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
        while True:
            areas = self.jefeDeMesaController.obtenerAreas()
            
            self.mostrarAreas(areas)
            
            opcionesValidas = []
            for item in areas:
                opcionesValidas.append(item.id)

            opcionSalida = 0
            opcionesValidas.append(opcionSalida)

            text = " Ingresar n° de área a modificar (ingrese 0 volver atras): "
            idAreaModificar = GuiInputUtils.inputTextCustom(opcionesValidas, text)
            
            if idAreaModificar == 0:
                break
            else:
                for item in areas:
                    if(item.id == idAreaModificar):
                        area = item
                GuiUtils.clearTerminal()
                GuiUtils.titulo("Ejecutivo mesa de ayuda")
                GuiUtils.subtitulo(" modificación de área: " + area.nomArea)
                GuiUtils.subtitulo(" Por favor ingrese el detalle requerido: ")
                area.nomArea = input(" Nombre: ")
                area.dscArea = input(" Descripción: ")
                self.jefeDeMesaController.modificarArea(area)
                GuiUtils.clearTerminal()
                GuiUtils.tituloEspaciado("Área modificada correctamente")
                input(" Presione cualquier tecla continuar...")

    def eliminarAreas(self):
        while True:
            areas = self.jefeDeMesaController.obtenerAreas()
            
            self.mostrarAreas(areas)
            
            opcionesValidas = []
            for item in areas:
                opcionesValidas.append(item.id)

            opcionSalida = 0
            opcionesValidas.append(opcionSalida)

            text = " Ingresar n° de área a eliminar (ingrese 0 volver atras): "
            idAreaEliminar = GuiInputUtils.inputTextCustom(opcionesValidas, text)
            
            if idAreaEliminar == 0:
                break
            else:    
                eliminable = self.jefeDeMesaController.validarRelacionArea(idAreaEliminar)
                if eliminable:
                    #print("Se inicia la eliminacion del area")
                    self.jefeDeMesaController.eliminarArea(idAreaEliminar)
                    GuiUtils.clearTerminal()
                    GuiUtils.tituloEspaciado("Área eliminada correctamente")
                    input(" Presione cualquier tecla continuar...")
                    #print("Se elimino el area correctamente")
                else:
                    print("No se puede Eliminar el registro ya que cuenta tickets asignados")

    def mostrarAreas(self,areas):
        GuiUtils.clearTerminal()
        GuiUtils.titulo("Jefe de mesa de ayuda")
        GuiUtils.subtitulo(" Listado de áreas existentes")
        GuiUtils.espaciado()
        header = "|" + GuiUtils.customText(2, 9, " ", "ID")
        header += "|" + GuiUtils.customText(2, 88, " ", "Nombre") + "|"
        print(header)
        GuiUtils.espaciado()
        print("| " + GuiUtils.customText( 1, 97, " ", "Descripción") + "|")
        GuiUtils.espaciado()
        GuiUtils.separador()
        for item in areas:
            #print("| %3s  | %30s | %30s |"%(item.id, item.nomArea, item.dscArea))
            GuiUtils.espaciado()
            data = "|" + GuiUtils.customText(2, 9, " ", item.id)
            data += "|" + GuiUtils.customText(2, 88, " ", item.nomArea) + "|"
            print(data)
            GuiUtils.espaciado()
            print("| " + GuiUtils.customText( 1, 97, " ", item.dscArea) + "|")
            GuiUtils.espaciado()
            GuiUtils.separador()       
    
    def mostrarAreasSimple(self,areas):
        GuiUtils.clearTerminal()
        GuiUtils.titulo("Jefe de mesa de ayuda")
        GuiUtils.subtitulo(" Listado de áreas existentes")
        header = "|" + GuiUtils.customText(2, 49, " ", "ID")
        header += "|" + GuiUtils.customText(2, 48, " ", "Nombre") + "|"
        print(header)
        GuiUtils.separador()
        for item in areas:
            #print("| %3s  | %30s | %30s |"%(item.id, item.nomArea, item.dscArea))
            data = "|" + GuiUtils.customText(2, 49, " ", item.id)
            data += "|" + GuiUtils.customText(2, 48, " ", item.nomArea) + "|"
            print(data)
            GuiUtils.separador()       

    def menuOpciones(self):
        
        GuiUtils.clearTerminal()
        GuiUtils.titulo("Jefe de mesa de ayuda")
        GuiUtils.subtitulo("Menu de opciones para áreas ")
        GuiUtils.izq("1) Crear área")
        GuiUtils.izq("2) Modificar área")
        GuiUtils.izq("3) Eliminar área")
        GuiUtils.izq("0) Volver")
        GuiUtils.separador()
        opcionesValidas = [0,1,2,3]
        value = int(input(" Ingrese un n° de opción para continuar: "))
        if value in opcionesValidas:
            return value