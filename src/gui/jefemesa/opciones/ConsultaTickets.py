from datetime import datetime
from controller.JefeDeMesaController import JefeDeMesaController
from gui.OpcioensComunes import OpcionesComunes
from utils.GuiInputUtils import GuiInputUtils
from utils.GuiUtils import GuiUtils


class ConsultaTickets:
    
    def __init__(self):
        self.jefeDeMesaController = JefeDeMesaController._jefeDeMesaController 
        pass
    
    def start(self):
        GuiUtils.clearTerminal()
        while True:
            GuiUtils.clearTerminal()
            opcion =self.opciones()
            GuiUtils.clearTerminal()
            if opcion ==1:
                self.conslutarPorFecha()
                pass
            elif opcion == 2:
                self.conslutaPorCriticidad()
                pass
            elif opcion == 3:
                self.consultarTipoTicket()
                pass
            elif opcion == 4:
                self.consultarEjecutivoCreacion()
                pass
            elif opcion == 5:
                pass
            elif opcion == 6:
                pass
            elif opcion == 7:
                break

    def conslutarPorFecha(self):
        fecha = datetime.now()
        while True:
            print("ingrese la fecha que desea buscar")
            print("ingrese el dia: ")
            dia = GuiInputUtils.inputNumberNoParams()
            print("ingrese el mes: ")
            mes= GuiInputUtils.inputNumberNoParams()
            print("ingrese el año: ")
            anno = GuiInputUtils.inputNumberNoParams()
            try:
                fecha = datetime(year=anno,month=mes, day=dia)
                break
            except Exception as error :
                print("la fecha ingresada no es correcta, intente nuevamente")
                pass
        tickets  = self.jefeDeMesaController.buscarTicketsPorFechaCreacion(fecha)
        self.mostrarTickets(tickets)
        OpcionesComunes.presioneEnterContinuar()

    def conslutaPorCriticidad(self):
        while True:
            GuiUtils.clearTerminal()
            print("Lista de Criticidades")
            print()
            criticidades=   self.jefeDeMesaController.obtenerCriticidades()
            self.mostrarCriticidades(criticidades)
      
            opcionesValidas = []
            for item in criticidades:
                opcionesValidas.append(item.id)
            opcionSalida = 0
            opcionesValidas.append(opcionSalida)
            print("Ingrese el id del Criticidad a que desea buscar (ingrese 0 para salir)")
            idArea =GuiInputUtils.inputNumber(opcionesValidas)
            if idArea ==0:
                break
            else:
                GuiUtils.clearTerminal()
                tickets =   self.jefeDeMesaController.buscarTicketsPorCriticidad(idArea)
                self.mostrarTickets(tickets)
                OpcionesComunes.presioneEnterContinuar()

    def consultarTipoTicket(self):
        while True:
            GuiUtils.clearTerminal()
            print("Lista de Tipos de Ticket")
            print()
            tiposTicket=   self.jefeDeMesaController.obtenerTiposTicket()
            OpcionesComunes.mostrarTipoTicket(tiposTicket)
      
            opcionesValidas = []
            for item in tiposTicket:
                opcionesValidas.append(item.id)
            opcionSalida = 0
            opcionesValidas.append(opcionSalida)
            print("Ingrese el id del Tipo de Ticket que desea buscar (ingrese 0 para salir)")
            idTipoTicket =GuiInputUtils.inputNumber(opcionesValidas)
            if idTipoTicket ==0:
                break
            else:
                GuiUtils.clearTerminal()
                tickets =   self.jefeDeMesaController.buscarTicketsPoTipoTicket(idTipoTicket)
                self.mostrarTickets(tickets)
                OpcionesComunes.presioneEnterContinuar()
    
    def consultarEjecutivoCreacion(self):
        while True:
            GuiUtils.clearTerminal()
            print("Lista de Ejcutivos")
            print()
            ejecutivos=   self.jefeDeMesaController.obtenerEjecutivosMesa()
            OpcionesComunes.mostarUsuarios(ejecutivos)
      
            opcionesValidas = []
            for item in ejecutivos:
                opcionesValidas.append(item.id)
            opcionSalida = 0
            opcionesValidas.append(opcionSalida)
            print("Ingrese el id del Usuario que desea buscar (ingrese 0 para salir)")
            idUsuario =GuiInputUtils.inputNumber(opcionesValidas)
            if idUsuario ==0:
                break
            else:
                GuiUtils.clearTerminal()
                tickets =   self.jefeDeMesaController.buscarTicketsPorUsuarioCreacion(idUsuario)
                self.mostrarTickets(tickets)
                OpcionesComunes.presioneEnterContinuar()   
            
    def mostrarCriticidades(self,criticidades):
        HEADER = "|  ID  |    Nombre Criticidad   |  Descripcion Criticidad   |"
        print(HEADER)
        
        for item in criticidades:
            print("| %3s  | %30s | %30s |"%(item.id, item.nomCriticidad, item.dscCriticidad))
    def mostrarTickets(slef, tickets):
        HEADER =  "| ID  | Ejecutivo Creacion        |      Fecha Creacion       |     Tipo Ticket      |      Criticidad     |     Area    |     Estado     | "
           
        print(HEADER)
        for item in tickets:
            row ="| %3s | %25s | %25s | %20s | %17s  | %13s |  %10s|"%(
                item.idTicket,
                item.nombreUsuarioCreacion,
                item.fechaCreacion,
                item.nomTipoTicket,
                item.nomArea,
                item.nomCriticidad,
                item.nomEstado
                )
            print(row)
    def opciones(self):
        print(GuiUtils.subrrayar("   Opciones  "))
        print()
        print("1). Filtrar Por Fecha Especifica")
        print("2). Filtrar Por Criticidad")
        print("3). Filtrar Por Tipo Ticket")
        print("4). Filtrar Por Ejecutivo que Abre el Ticket")
        print("5). Filtrar Por Ejecutivo que Cierra el Ticket")
        print("6). Filtrar Por Area ")
        print("7). Atras ")
        
        
        opcionesValidas = [1,2,3,4,5,6,7]
        opcion = GuiInputUtils.inputNumber(opcionesValidas)
        return opcion