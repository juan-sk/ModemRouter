import logging
from service.TicketService import TicketService


class EjecutivoEspecificoController:
    
    def __init__(self):
        self.ticketService = TicketService._ticketService()
    
        pass
    def obtenerTicketsAsignados(self, idUsuario):
        return self.ticketService.obtenerTicketsAsignados(idUsuario)
    
    def obtenerEstadoTicket(self):
        return self.ticketService.obtenerEstadosTicket()
    
    def guardarTicket(self, ticket):
        try:
            return self.ticketService.actualizarTicket(ticket)
        except Exception as error:
            logging.error(error)
    @staticmethod(function)            
    def build():
        EjecutivoEspecificoController._ejecutivoEspecificoController = EjecutivoEspecificoController()