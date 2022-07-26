import logging
from entity.TipoTicketEntity import TipoTicketEntity
from controller.JefeDeMesaController import JefeDeMesaController
from gui.OpcioensComunes import OpcionesComunes
from utils.GuiInputUtils import GuiInputUtils
from utils.GuiUtils import GuiUtils


class GestionarTiposTicket:
    
    def __init__(self):
        self.jefeDeMesaController = JefeDeMesaController._jefeDeMesaController 
     
        pass
    
    def start(self):
        
        while True:
            
            
            opcion = self.menuOpciones()
                         
            if opcion == 1:
                self.creaTipoTicket()
            elif opcion == 2:
                self.modificaTipoTicket()
            elif opcion == 3:
                self.eliminaTipoTicket()
                pass
            elif opcion == 0:
                break
        
        
    def menuOpciones(self):
        GuiUtils.clearTerminal()
        GuiUtils.titulo("Jefe de mesa de ayuda")
        GuiUtils.subtitulo("Menu de opciones para tipos de ticket ")
        GuiUtils.izq("1) Crear tipo de ticket")
        GuiUtils.izq("2) Modificar tipo de ticket")
        GuiUtils.izq("3) Eliminar tipo de ticket")
        GuiUtils.izq("0) Volver")
        GuiUtils.separador()
        opcionesValidas = [0,1,2,3]
        value = int(input(" Ingrese un n° de opción para continuar: "))
        if value in opcionesValidas:
            return value
    
    def creaTipoTicket(self):
        while True:
            GuiUtils.clearTerminal()
            GuiUtils.titulo("Jefe de mesa de ayuda")
            GuiUtils.subtitulo(" Creación de tipo de ticket")
            GuiUtils.subtitulo(" Por favor ingrese el detalle requerido: ")
            tipoT = TipoTicketEntity()
            tipoT.nomTipoTicket = input(" Nombre: ")
            tipoT.dscTipoTicket = input(" Descripción: ")
            try:
                self.jefeDeMesaController.guardarTipoTicket(tipoT)
                GuiUtils.clearTerminal()
                GuiUtils.tituloEspaciado("Tipo de ticket creado correctamente")
                input(" Presione cualquier tecla continuar...")
                break
            except Exception as error:
                logging.error("ocurrio un error el el guardado del tipo de ticket")
                logging.error(error)
                print("ocurrio un error al guardar El Tipo de Ticket ")
                print("Desea Intentar Nuevamente? (si/no)")
                respuesta = GuiInputUtils.inputSiNo()
                if respuesta == 1:
                    continue
                else:
                    break       

     
    def modificaTipoTicket(self):
        while True:
            tiposTickets = self.jefeDeMesaController.obtenerTiposTicket()
            self.mostrarTipoTicket(tiposTickets)
            
            opcionesValidas = []
            for item in tiposTickets:
                opcionesValidas.append(item.id)
            opcionesValidas.append(0)
            text = "ingrese el id del tipo de ticket a modificar (ingrese 0 para volver atras): "
            idTipoTicketAModificar =GuiInputUtils.inputTextCustom(opcionesValidas, text)
            if(idTipoTicketAModificar == 0):
                break
            else:
                try:
                    for item in tiposTickets:
                        if(item.id == idTipoTicketAModificar):
                            tipoTicket = item
                    GuiUtils.clearTerminal()
                    GuiUtils.titulo("Ejecutivo mesa de ayuda")
                    GuiUtils.subtitulo(" Modificación de tipo de ticket: " + tipoTicket.nomTipoTicket)
                    GuiUtils.subtitulo(" Por favor ingrese el detalle requerido: ")
                    tipoTicket.nomTipoTicket = input(" Nombre: ")
                    tipoTicket.dscTipoTicket = input(" Descripción: ")
                    self.jefeDeMesaController.modificarTipoTicket(tipoTicket)
                    GuiUtils.clearTerminal()
                    GuiUtils.tituloEspaciado("Tipo de ticket modificado correctamente")
                    input(" Presione cualquier tecla continuar...")
                except Exception as error :
                    print("ocurrio un error al guardar la modificacion del tipo de ticket")
                    logging.error(error)

    def eliminaTipoTicket(self):
        while True:
            try:
                tiposTickets = self.jefeDeMesaController.obtenerTiposTicket()
                self.mostrarTipoTicket(tiposTickets)
                
                opcionesValidas = []
                for item in tiposTickets:
                    opcionesValidas.append(item.id)
                    
                opcionesValidas.append(0)

                text = " Ingresar n° de tipo de ticket a eliminar (ingrese 0 volver atras): "
                idTipoTicketAEliminar =GuiInputUtils.inputTextCustom(opcionesValidas, text)

                if idTipoTicketAEliminar == 0:
                    break
                else:    
                    eliminable = self.jefeDeMesaController.tipoTicketEliminable(idTipoTicketAEliminar)
                    if eliminable:        
                        self.jefeDeMesaController.eliminarTipoTicket(idTipoTicketAEliminar)
                        GuiUtils.clearTerminal()
                        GuiUtils.tituloEspaciado("Tipo de ticket eliminado correctamente")
                        input(" Presione cualquier tecla continuar...")
                    else:
                        GuiUtils.clearTerminal()
                        GuiUtils.tituloEspaciado("El Tipo de Ticket no se puede eliminar ya que cuenta con tickets Asignados")
                        input(" Presione cualquier tecla continuar...")
            except Exception as error:
                logging.error(error)
                print("ocurrrio un error al intentar Eliminar el Tipo de Ticket")
       
    def mostrarTipoTicket(self,tiposTickets):
        GuiUtils.clearTerminal()
        GuiUtils.titulo("Jefe de mesa de ayuda")
        GuiUtils.subtitulo(" Listado de tipos de tickets existentes")
        GuiUtils.espaciado()
        header = "|" + GuiUtils.customText(2, 9, " ", "ID")
        header += "|" + GuiUtils.customText(2, 88, " ", "Nombre") + "|"
        print(header)
        GuiUtils.espaciado()
        print("| " + GuiUtils.customText( 1, 97, " ", "Descripción") + "|")
        GuiUtils.espaciado()
        GuiUtils.separador()
        for item in tiposTickets:
            #print("| %3s  | %30s | %30s |"%(item.id, item.nomArea, item.dscArea))
            GuiUtils.espaciado()
            data = "|" + GuiUtils.customText(2, 9, " ", item.id)
            data += "|" + GuiUtils.customText(2, 88, " ", item.nomTipoTicket) + "|"
            print(data)
            GuiUtils.espaciado()
            print("| " + GuiUtils.customText( 1, 97, " ", item.dscTipoTicket) + "|")
            GuiUtils.espaciado()
            GuiUtils.separador()       