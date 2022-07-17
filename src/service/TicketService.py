from re import I
from pojo.Ticket import Ticket
from repository.AreaRepository import AreaRepository
from repository.CriticidadRepository import CriticidadRepository
from repository.EstadoTicketRepository import EstadoTicketRepository
from repository.TicketRepository import TicketRepository
from repository.TipoTicketRepository import TipoTicketRepository


class TicketService:
    
    def __init__(self):
        self.ticketRepo = TicketRepository()
        self.criticidadRepo = CriticidadRepository()
        self.areaRepo = AreaRepository()
        self.tipoTicketRepo = TipoTicketRepository()
        self.estadoTicket = EstadoTicketRepository()
        
        
    def guardarTicket(self,ticket):
        return self.ticketRepo.guardarTicket(ticket)
    def actualizarTicket(self,ticket):
        return self.ticketRepo.actualizarTicket(ticket)
    
    def obtenerCriticidades(self):
        return self.criticidadRepo.obtenerCriticidades()
    
    def obenerAreas(self):
        return self.areaRepo.obtenerAreas();
    
    
    def obtenerTiposTickets(self):
        return self.tipoTicketRepo.obtenerTipoTickets()
    
    def obtenerTicketsAsignados(self,idUsuario):
        tickets =self.ticketRepo.obtenerTicketsUsuario(idUsuario)
        return tickets
    def obtenerEstadosTicket(self):
        return self.estadoTicket.obtenerEstadosTicket()
                
        

             
    