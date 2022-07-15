import logging
from service.TicketService import TicketService


class EjecutivoMesaController:
    
    
    def __init__(self):
        self.ticketService = TicketService()
        pass
    
    def crearTicket(self, ticket):
        try:
            return self.ticketService.guardarTicket(ticket)
        except Exception as error:
            logging.errro