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
              
            GuiUtils.clearTerminal()
            
            opcion = self.menuOpciones()
            if opcion == 1:
                self.creaTipoTicket()
            #elif opcion ==2:
            #    self.modificaTipoTicket()
            elif opcion == 2:
                self.eliminaTipoTicket()
                pass
            elif opcion == 3:
                break
        
        
    def menuOpciones(self):
  
        print(GuiUtils.subrrayar("Opciones: ")) 
        print("")            
        print("1). Crear Tipo Ticket")            
        #print("2). Modificar Tipo Ticket")            
        print("2). Eliminar Tipo Ticket")            
        print("3). Atras")            
        print("")            
        opcionsValidas = [1,2,3]
        return GuiInputUtils.inputNumber(opcionsValidas)
    
    
    def creaTipoTicket(self):
        while True:
            GuiUtils.clearTerminal()
            print(GuiUtils.subrrayar("Crear tipo ticket"))
            tipoT = TipoTicketEntity()
            tipoT.nomTipoTicket = input("Ingrese El nombre del Tipo de Ticket: ")
            tipoT.dscTipoTicket = input("ingrese la descripcion del Tipo de Ticket: ")
            tipoT.print()
            OpcionesComunes.presioneEnterContinuar()
            try:
                print("Comienza el Guardado del tipo del ticket")
                self.jefeDeMesaController.guardarTipoTicket(tipoT)
                print("Se Termino el guardao del ticket")
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
        OpcionesComunes.presioneEnterContinuar()
          
          

             
    def modificaTipoTicket(self):
        tiposTickets = self.jefeDeMesaController.obtenerTiposTicket()
        self.mostrarTipoTicket(tiposTickets)
        
        opcionesValidas = []
        for item in tiposTickets:
            opcionesValidas.append(item.id)
        opcionesValidas.append(0)
        print("ingrese el id del registro a modificar (ingrese 0 para salir)")
        idTipoTicketAModificar =GuiInputUtils.inputNumber(opcionesValidas)
        if(idTipoTicketAModificar == 0):
            return 
        else:
            try:
                
            
                tipot = TipoTicketEntity()
                tipot.id = idTipoTicketAModificar
                print("Nombre Anterior del Tipo Ticket: %s"%tipot.nomTipoTicket)
                tipot.nomTipoTicket  = input("ingrese el nuevo Nombre para el Tipo de ticket: ")
                
                print("Descripcion Anterior del Tipo de Ticket: %s"%tipot.dscTipoTicket)
                tipot.dscTipoTicket = input("ingrese la nueva Descripcion para el Tipo de Ticket: ")
                
                input("Presione enter para continuar con el guardado del ticket")
                print("Inicia el guardaod del Tipo de Ticket")
                self.jefeDeMesaController.modificarTipoTicket(tipot)
                print("Se Guardo Correctamente el Tipo de Ticket")
            except Exception as error :
                print("ocurrio un error al guardar la modificacion del tipo de ticket")
                logging.error(error)
            OpcionesComunes.presioneEnterContinuar()
        pass

    def eliminaTipoTicket(self):
        while True:
            try:
                tiposTickets = self.jefeDeMesaController.obtenerTiposTicket()
                self.mostrarTipoTicket(tiposTickets)
                
                opcionesValidas = []
                for item in tiposTickets:
                    opcionesValidas.append(item.id)
                    
                opcionesValidas.append(0)

                print("ingrese el id del registro a modificar (ingrese 0 para salir)")
                idTipoTicketAEliminar =GuiInputUtils.inputNumber(opcionesValidas)

                if idTipoTicketAEliminar == 0:
                    break
                else:    
                    eliminable = self.jefeDeMesaController.tipoTicketEliminable(idTipoTicketAEliminar)
                    if eliminable:        
                        print("Se inicia la eliminacion del tipo de ticket")
                        self.jefeDeMesaController.eliminarTipoTicket(idTipoTicketAEliminar)
                        print("Se elimino el tipo de ticket correctamente")
                        
                    else:
                        print("El Tipo de Ticket no se puede eliminar ya que cuenta con Tickets Asignado")
                    OpcionesComunes.presioneEnterContinuar()
            except Exception as error:
                logging.error(error)
                print("ocurrrio un error al intentar Eliminar el Tipo de Ticket")
            
        OpcionesComunes.presioneEnterContinuar()
       
    def mostrarTipoTicket(self,tiposTickets):
        GuiUtils.clearTerminal()
        print(GuiUtils.subrrayar("Listado de tipos de ticket"))
        HEADER = "|  ID  |    Nombre   |  Descripcion   |"
        print(HEADER)        
        for item in tiposTickets:
            print("| %3s  | %30s | %30s |"%(item.id, item.nomTipoTicket, item.dscTipoTicket))