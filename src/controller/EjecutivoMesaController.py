import logging
from service.TicketService import TicketService
from service.UsuarioService import UsuarioService


class EjecutivoMesaController:
    
    
    def __init__(self):
        self.ticketService = TicketService()
        self.usuarioService = UsuarioService()

        pass
    
    def crearTicket(self, ticket):
        try:
            return self.ticketService.guardarTicket(ticket)
        except Exception as error:
            logging.error(error)
            
    def obtenerCriticidadesTicket(self):
        return self.ticketService.obtenerCriticidades()
    
    def obtenerAreaTicket(self):
        return self.ticketService.obenerAreas()
    
    def obtenerTiposTickets(self):
        return self.ticketService.obtenerTiposTickets()
    def obtenerUsuarios(self, idArea):
        return self.usuarioService.obtenerUsuarioPorArea(idArea)