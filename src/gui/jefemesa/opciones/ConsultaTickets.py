from cgi import print_arguments
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
        
        while True:
            
            opcion = self.opciones()

            if opcion == 1:
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
                self.consultarEjecutivoCierre()
                pass
            elif opcion == 6:
                self.consultarPorArea()
            elif opcion == 0:
                break

    def conslutarPorFecha(self):
        fecha = datetime.now()
        while True:
            GuiUtils.clearTerminal()
            GuiUtils.titulo("Ejecutivo mesa de ayuda")
            GuiUtils.subtitulo(" Busqueda de tickets según fecha especifica")
            day = int(input(" Día: "))
            month = int(input(" Mes: "))
            year = int(input(" Año: "))
            try:
                fecha = datetime(year = year, month = month, day = day)
                break
            except Exception as error:
                GuiUtils.clearTerminal()
                GuiUtils.tituloEspaciado("la fecha ingresada no es correcta, intente nuevamente")
                pass
        tickets = self.jefeDeMesaController.buscarTicketsPorFechaCreacion(fecha)
        self.mostrarTickets(tickets)

    def conslutaPorCriticidad(self):
        while True:
            criticidades = self.jefeDeMesaController.obtenerCriticidades()
            self.mostrarCriticidades(criticidades)
      
            opcionesValidas = []
            for item in criticidades:
                opcionesValidas.append(item.id)
            opcionSalida = 0
            opcionesValidas.append(opcionSalida)
            text = "Ingrese el id del Criticidad a que desea buscar (ingrese 0 volver atras): "
            idCriticidad =GuiInputUtils.inputTextCustom(opcionesValidas, text)
            if idCriticidad == 0:
                break
            else:
                tickets = self.jefeDeMesaController.buscarTicketsPorCriticidad(idCriticidad)
                self.mostrarTickets(tickets)

    def consultarTipoTicket(self):
        while True:
            tiposTicket = self.jefeDeMesaController.obtenerTiposTicket()
            OpcionesComunes.mostrarTipoTicket(tiposTicket)
      
            opcionesValidas = []
            for item in tiposTicket:
                opcionesValidas.append(item.id)
            opcionSalida = 0
            opcionesValidas.append(opcionSalida)
            text = " Ingrese el id del Tipo de Ticket que desea buscar (ingrese 0 volver atras): "
            idTipoTicket =GuiInputUtils.inputTextCustom(opcionesValidas, text)
            if idTipoTicket ==0:
                break
            else:
                tickets =   self.jefeDeMesaController.buscarTicketsPoTipoTicket(idTipoTicket)
                self.mostrarTickets(tickets)

    def consultarEjecutivoCreacion(self):
        while True:
            ejecutivos =  self.jefeDeMesaController.obtenerUsuarios()
            self.mostarUsuarios(ejecutivos)
      
            opcionesValidas = []
            for item in ejecutivos:
                opcionesValidas.append(item.id)
            opcionSalida = 0
            opcionesValidas.append(opcionSalida)
            text = " Ingrese el id del usuario que desea buscar (ingrese 0 volver atras): "
            idUsuario =GuiInputUtils.inputTextCustom(opcionesValidas, text)
            if idUsuario ==0:
                break
            else:
                tickets =   self.jefeDeMesaController.buscarTicketsPorUsuarioCreacion(idUsuario)
                self.mostrarTickets(tickets)
    
    def consultarEjecutivoCierre(self):
        while True:
            ejecutivos =  self.jefeDeMesaController.obtenerUsuarios()
            self.mostarUsuarios(ejecutivos)
      
            opcionesValidas = []
            for item in ejecutivos:
                opcionesValidas.append(item.id)
            opcionSalida = 0
            opcionesValidas.append(opcionSalida)
            text = "Ingrese el id del usuario que desea buscar (ingrese 0 volver atras): "
            idUsuario =GuiInputUtils.inputTextCustom(opcionesValidas, text)
            if idUsuario == 0:
                break
            else:
                tickets =   self.jefeDeMesaController.buscarTicketsPorUsuarioCierre(idUsuario)
                self.mostrarTickets(tickets)
                
    def consultarPorArea(self):
        while True:
            areas =  self.jefeDeMesaController.obtenerAreas()
            self.mostrarAreas(areas)
      
            opcionesValidas = []
            for item in areas:
                opcionesValidas.append(item.id)
            opcionSalida = 0
            opcionesValidas.append(opcionSalida)
            text = " Ingrese el N° del area por el que desae buscar (ingrese 0 volver atras): "
            idArea = GuiInputUtils.inputTextCustom(opcionesValidas, text)
            if idArea == 0:
                break
            else:
                tickets =   self.jefeDeMesaController.buscarTicketsPorArea(idArea)
                self.mostrarTickets(tickets)
    
    def mostarUsuarios(self,ejecutivos):
        GuiUtils.clearTerminal()
        GuiUtils.titulo("Jefe de mesa de ayuda")
        GuiUtils.subtitulo(" Listado de usuarios existentes")
        header = "|" + GuiUtils.customText(2, 9, " ", "ID")
        header += "|" + GuiUtils.customText(2, 88, " ", "Nombre de usuario") + "|"
        print(header)
        GuiUtils.separador()
        for item in ejecutivos:
            #print("| %3s  | %30s | %30s |"%(item.id, item.nomArea, item.dscArea))
            data = "|" + GuiUtils.customText(2, 9, " ", item.id)
            data += "|" + GuiUtils.customText(2, 88, " ", item.nombreUsuario) + "|"
            print(data)
            GuiUtils.separador()  

    def mostrarCriticidades(self, criticidades):
        GuiUtils.clearTerminal()
        GuiUtils.titulo("Jefe de mesa de ayuda")
        GuiUtils.subtitulo(" Listado de criticidades existentes")
        header = "|" + GuiUtils.customText(2, 9, " ", "ID")
        header += "|" + GuiUtils.customText(2, 88, " ", "Nombre") + "|"
        print(header)
        GuiUtils.separador()
        for item in criticidades:
            #print("| %3s  | %30s | %30s |"%(item.id, item.nomArea, item.dscArea))
            data = "|" + GuiUtils.customText(2, 9, " ", item.id)
            data += "|" + GuiUtils.customText(2, 88, " ", item.nomCriticidad) + "|"
            print(data)
            GuiUtils.separador()  

    def mostrarAreas(self,areas):
        GuiUtils.clearTerminal()
        GuiUtils.titulo("Jefe de mesa de ayuda")
        GuiUtils.subtitulo(" Listado de áreas existentes")
        header = "|" + GuiUtils.customText(2, 9, " ", "ID")
        header += "|" + GuiUtils.customText(2, 88, " ", "Nombre") + "|"
        print(header)
        GuiUtils.separador()
        for item in areas:
            #print("| %3s  | %30s | %30s |"%(item.id, item.nomArea, item.dscArea))
            data = "|" + GuiUtils.customText(2, 9, " ", item.id)
            data += "|" + GuiUtils.customText(2, 88, " ", item.nomArea) + "|"
            print(data)
            GuiUtils.separador()  
    
    def mostrarTickets(self, tickets):
        if(len(tickets) > 0):
            GuiUtils.clearTerminal()
            GuiUtils.titulo("Jefe de mesa de ayuda")
            GuiUtils.subtitulo(" Listado de tickets")
            header = "|" + GuiUtils.customText(2, 5, " ", "ID")
            header += "|" + GuiUtils.customText(2, 21, " ", "Fecha creación")
            header += "|" + GuiUtils.customText(2, 15, " ", "Tipo ticket")
            header += "|" + GuiUtils.customText(2, 12, " ", "Criticidad")
            header += "|" + GuiUtils.customText(2, 27, " ", "Area")
            header += "|" + GuiUtils.customText(2, 13, " ", "Estado") + "|"
            print(header)
            GuiUtils.separador()
            for item in tickets:
                data = "|" + GuiUtils.customText(2, 5, " ", item.idTicket)
                data += "|" + GuiUtils.customText(2, 21, " ", item.fechaCreacion)
                data += "|" + GuiUtils.customText(2, 15, " ", item.nomTipoTicket)
                data += "|" + GuiUtils.customText(2, 12, " ", item.nomCriticidad)
                data += "|" + GuiUtils.customText(2, 27, " ", item.nomArea)
                data += "|" + GuiUtils.customText(2, 13, " ", item.nomEstado) + "|"
                #print("| %3s  | %30s | %30s |"%(item.id, item.nomArea, item.dscArea))
                #data = "|" + GuiUtils.customText(2, 9, " ", item.id)
                #data += "|" + GuiUtils.customText(2, 88, " ", item.nomArea) + "|"
                print(data)
            GuiUtils.separador()
        else:
            GuiUtils.clearTerminal()
            GuiUtils.tituloEspaciado("No se han encontrado resultados")
        input(" Presione cualquier tecla continuar...")
        
    def opciones(self):

        GuiUtils.clearTerminal()
        GuiUtils.titulo("Jefe de mesa de ayuda")
        GuiUtils.subtitulo("Menu de opciones para consulta de tickets")
        GuiUtils.izq("1) Filtrar Por Fecha Especifica")
        GuiUtils.izq("2) Filtrar Por Criticidad")
        GuiUtils.izq("3) Filtrar Por Tipo Ticket")
        GuiUtils.izq("4) Filtrar Por Ejecutivo que Abre el Ticket")
        GuiUtils.izq("5) Filtrar Por Ejecutivo que Cierra el Ticket")
        GuiUtils.izq("6) Filtrar Por Area ")
        GuiUtils.izq("0) Volver ")
        GuiUtils.separador()
        opcionesValidas = [0,1,2,3,4,5,6]
        value = int(input(" Ingrese un n° de opción para continuar: "))
        if value in opcionesValidas:
            return value