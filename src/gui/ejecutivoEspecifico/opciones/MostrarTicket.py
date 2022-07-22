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
        tickets = self.ejecutivoEspecificoController.obtenerTicketsAsignados(idUsuario)

   
        self.mostrarTickets(tickets)
        ticket =  self.ticketARevisar(tickets)
        self.imprimirTicket(ticket)
        input("Presione Enter para Continuar ...")
        
        ticket.observacion = input("Observacion: ")
        estadosTicket = self.ejecutivoEspecificoController.obtenerEstadoTicket()
        ticket.idEstado = self.seleccionarEstadoTicket(estadosTicket)
        
        GuiUtils.clearTerminal()
        print("Guardando ticket..")
        ticketEntity =   TicketEntity.fromTicket(ticket)
        self.ejecutivoEspecificoController.guardarTicket(ticketEntity)
        print("el ticket fue guardado")
        input("Presione Enter para Continuar ...")
        
        
    def seleccionarEstadoTicket(self, estadosTicket):
        GuiUtils.clearTerminal()
        while True:
            try:
                print(GuiUtils.subrrayar(" Estados Ticket"))
                opcionesTicket = []
                for item in estadosTicket:
                    opcionesTicket.append(item.id)
                    print("%d). %s"%(item.id,item.nomEstadoTicket))
                    
                opcion = input("ingrese Opcion: ")
                opcionInt = int(opcion)
                if opcionInt in opcionesTicket:
                    return item.id
            except Exception as error:
                logging.error("ocurrio un error seleccionando el estado del ticket")
                logging.error(error)
    def imprimirTicket(self, t):
        GuiUtils.clearTerminal()
        ticket = """
            Ticket %s
            
            Usuario Creacion:%s
            Usuario Derivado:%s
            Criticidad:      %s
            Area:            %s
            Tipo Ticket:     %s
            Estado Ticket:   %s
            
            
            Nombre Cliente:  %s
            Rut Cliente :    %s
            Telefono Cliente:%s
            Detalle: 
            %s
            
            Observacion:
            %s
            
            feha Creacion   %s
                   
        """%(
            t.idTicket,
            t.nombreUsuarioCreacion,
            t.nombreUsuarioDerivado,
            t.nomCriticidad,
            t.nomArea,
            t.nomTipoTicket,
            t.nomEstado,
            t.nombreCliente,
            t.rutCliente ,
            t.telefono,
            t.detalle,
            t.observacion,
            t.fechaCreacion
        )
        print(ticket)
        
        
    def ticketARevisar(self,tickets):
        while True:
            try:
                
                opcion = input("ingrese Ticket Para Revisar:")
                opcionInt =int(opcion)
                for item in tickets:
                     
                    if opcionInt == item.idTicket:
                        return item

            except Exception as error:
                pass

    def mostrarTickets(self,tickets):
        GuiUtils.clearTerminal()
        try:
            HEADER = "|  ID   | Criticidad | Tipo Ticket | Nombre Cliente"
            print(HEADER)
            for item in tickets:
                printString  = "| %s  | %s    | %s    | %s     |"%(item.idTicket,item.nomCriticidad,item.nomTipoTicket,item.nombreCliente)
                
                print (printString)
                
        except Exception as error:
            logging.error("ocurrio un error al mostrar los tickets")
            logging.error(error)
             
