from repository.AreaRepository import AreaRepository
from repository.CriticidadRepository import CriticidadRepository
from repository.TicketRepository import TicketRepository
from repository.TipoTicketRepository import TipoTicketRepository


class TicketService:
    
    def __init__(self):
        self.ticketRepo = TicketRepository()
        self.criticidadRepo = CriticidadRepository()
        self.areaRepo = AreaRepository()
        self.tipoTicketRepo = TipoTicketRepository()
        
        
    def guardarTicket(self,ticket):
        return self.ticketRepo.guardarTicket(ticket)
    
    def obtenerCriticidades(self):
        return self.criticidadRepo.obtenerCriticidades()
    
    def obenerAreas(self):
        return self.areaRepo.obtenerAreas();
    
    
    def obtenerTiposTickets(self):
        return self.tipoTicketRepo.obtenerTipoTickets()