import logging
from controller.EjecutivoEspecificoController import EjecutivoEspecificoController
from entity.TicketEntity import TicketEntity
from utils.GuiInputUtils import GuiInputUtils
from utils.GuiUtils import GuiUtils 

class MostrarTicket:
    
    def __init__(self):
        self.ejecutivoEspecificoController = EjecutivoEspecificoController._ejecutivoEspecificoController
        pass
    
    def start(self,idUsuario):
        self.visualizarTickets(idUsuario)

    def visualizarTickets(self, idUsuario):
        while True:
            tickets = self.ejecutivoEspecificoController.obtenerTicketsAsignados(idUsuario)
            self.mostrarTickets(tickets)
            opcionesValidas = []
            for item in tickets:
                opcionesValidas.append(item.idTicket)
            opcionesValidas.append(0)
            text = " Ingresar n° de ticket a gestionar (0 para volver atras): "
            idTicket = GuiInputUtils.inputTextCustom(opcionesValidas, text)
            if(idTicket == 0):
                break
            else:
                for item in tickets:
                    if(item.idTicket == idTicket):
                        ticket = item
                self.imprimirTicket(ticket)
                GuiUtils.subtitulo("Acciones disponibles sobre el ticket")
                GuiUtils.espaciado()
                GuiUtils.izq("1) Escribir gestion realizada en el ticket")
                GuiUtils.izq("0) Volver")
                GuiUtils.espaciado()
                GuiUtils.separador()
                opcionesValidas  = [0, 1]
                editar = int(input(" Ingrese un n° de opción para continuar: "))
                if(editar == 0):
                    break
                else:
                    GuiUtils.clearTerminal()
                    GuiUtils.titulo("Ejecutivo especifico")
                    GuiUtils.subtitulo(" Por favor ingrese el detalle requerido: ")
                    ticket.observacion = input(" Observacion: ")
                    estadosTicket = self.ejecutivoEspecificoController.obtenerEstadoTicket()
                    ticket.idEstado = self.seleccionarEstadoTicket(estadosTicket)
                    ticketEntity =   TicketEntity.fromTicket(ticket)
                    self.ejecutivoEspecificoController.guardarTicket(ticketEntity)
                    GuiUtils.clearTerminal()
                    GuiUtils.tituloEspaciado("Ticket gestionado correctamente")
                    input(" Presione cualquier tecla continuar...")
            
    def seleccionarEstadoTicket(self, estadosTicket):
        while True:
            try:
                GuiUtils.separador()
                opcionesTicket = []
                for item in estadosTicket:
                    #opcionesTicket.append(item.id)
                    #print("%d). %s"%(item.id,item.nomEstadoTicket))
                    opcionesTicket.append(item.id)
                    GuiUtils.izq("%d) %s"%(item.id,item.nomEstadoTicket))
                GuiUtils.separador()
                opcion = input(" Seleccione un estado para el ticket: ")
                opcionInt = int(opcion)
                for item in estadosTicket:
                    if item.id == opcionInt:
                        return opcionInt
            except Exception as error:
                logging.error("ocurrio un error seleccionando el estado del ticket")
                logging.error(error)

    def imprimirTicket(self, t):
        GuiUtils.clearTerminal()
        GuiUtils.titulo("Ejecutivo especifico")
        GuiUtils.subtitulo(" Ticket #%s"%t.idTicket)
        print("|" + GuiUtils.customText(2, 49, " ", "Fecha creación") + "|" + GuiUtils.customText(2, 48, " ", t.fechaCreacion) + "|")
        print("|" + GuiUtils.customText(2, 49, " ", "Usuario creación") + "|" + GuiUtils.customText(2, 48, " ", t.nombreUsuarioCreacion) + "|")
        print("|" + GuiUtils.customText(2, 49, " ", "Usuario derivado") + "|" + GuiUtils.customText(2, 48, " ", t.nombreUsuarioDerivado) + "|")
        print("|" + GuiUtils.customText(2, 49, " ", "Criticidad") + "|" + GuiUtils.customText(2, 48, " ", t.nomCriticidad) + "|")
        print("|" + GuiUtils.customText(2, 49, " ", "Área") + "|" + GuiUtils.customText(2, 48, " ", t.nomArea) + "|")
        print("|" + GuiUtils.customText(2, 49, " ", "Tipo") + "|" + GuiUtils.customText(2, 48, " ", t.nomTipoTicket) + "|")
        print("|" + GuiUtils.customText(2, 49, " ", "Estado") + "|" + GuiUtils.customText(2, 48, " ", t.nomEstado) + "|")
        GuiUtils.separador()
        GuiUtils.subtitulo(" Detalle del cliente asociado:")
        print("|" + GuiUtils.customText(2, 49, " ", "Cliente") + "|" + GuiUtils.customText(2, 48, " ", t.nombreCliente) + "|")
        print("|" + GuiUtils.customText(2, 49, " ", "Rut") + "|" + GuiUtils.customText(2, 48, " ", t.rutCliente) + "|")
        print("|" + GuiUtils.customText(2, 49, " ", "Telefono") + "|" + GuiUtils.customText(2, 48, " ", t.telefono) + "|")
        GuiUtils.separador()
        GuiUtils.subtitulo(" Situación reportada: ")
        print("| " + GuiUtils.customText( 1, 97, " ", t.detalle) + "|")
        GuiUtils.separador()
        GuiUtils.subtitulo(" Observación del usuario especializado: ")
        print("| " + GuiUtils.customText( 1, 97, " ", t.observacion) + "|")
        GuiUtils.separador()
        
    def ticketARevisar(self,tickets):
        while True:
            try:
                
                opcion = input(" Ingresar n° de ticket a gestionar (0 para volver atras): ")
                opcionInt =int(opcion)
                for item in tickets:
                    if opcionInt == item.idTicket:
                        return item
            except Exception as error:
                pass

    def mostrarTickets(self,tickets):
        GuiUtils.clearTerminal()
        GuiUtils.titulo("Ejecutivo especifico")
        GuiUtils.subtitulo(" Listado de tickets en su bandeja")        
        try:
            header = "|" + GuiUtils.customText(2, 24, " ", "ID")
            header += "|" + GuiUtils.customText(2, 24, " ", "Criticidad")
            header += "|" + GuiUtils.customText(2, 24, " ", "Tipo Ticket")
            header += "|" + GuiUtils.customText(2, 23, " ", "Cliente") + "|"
            print(header)
            GuiUtils.separador()
            for item in tickets:
                #printString  = "| %s  | %s    | %s    | %s     |"%(item.idTicket,item.nomCriticidad,item.nomTipoTicket,item.nombreCliente)
                data = "|" + GuiUtils.customText(2, 24, " ", item.idTicket)
                data += "|" + GuiUtils.customText(2, 24, " ", item.nomCriticidad)
                data += "|" + GuiUtils.customText(2, 24, " ", item.nomTipoTicket)
                data += "|" + GuiUtils.customText(2, 23, " ", item.nombreCliente) + "|"    
                print(data)
            GuiUtils.separador()
        except Exception as error:
            logging.error("ocurrio un error al mostrar los tickets")
            logging.error(error)
             
