from repository.TicketRepository import TicketRepository


class TicketService:
    
    def __init__(self):
        self.ticketRepo = TicketRepository()
        
        
    def guardarTicket(self,ticket):
        return self.ticketRepo.guardarTicket(ticket)