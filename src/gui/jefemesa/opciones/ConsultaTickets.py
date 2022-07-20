from datetime import datetime
from controller.JefeDeMesaController import JefeDeMesaController
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
                input("presione Enter para continuar")
                pass
            elif opcion == 2:
                pass
            elif opcion == 3:
                pass
            elif opcion == 4:
                pass
            elif opcion == 5:
                pass
            elif opcion == 6:
                pass
            elif opcion == 7:
                break

    def mostrarTickets(slef, tickets):
        HEADER =  "| ID  | Ejecutivo Creacion        |      Fecha Creacion       | Tipo Ticket   | Criticidad |     Area    |   Estado    | "
           
        print(HEADER)
        for item in tickets:
            row ="| %3s | %25s | %25s | %20s | %15s  | %20s |  %10s"%(
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
        print("4). Filtrar Por Ejecutivo que abre el Ticket")
        print("5). Filtrar Por Ejecutivo que cierra el Ticket")
        print("6). Filtrar Por Area ")
        print("7). Atras ")
        
        
        opcionesValidas = [1,2,3,4,5,6,7]
        opcion = GuiInputUtils.inputNumber(opcionesValidas)
        return opcion