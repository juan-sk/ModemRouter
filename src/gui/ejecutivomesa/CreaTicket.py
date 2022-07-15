import logging

from controller.EjecutivoMesaController import EjecutivoMesaController
from pojo.Ticket import Ticket


class CreaTicket:
    
    def __init__(self):
        self.ejecutivoMesaController = EjecutivoMesaController()
    
    
    def start(self):
        ticket = self.formularioCreacionTicket()
        print("se Ingresaron los datos del ticket de manera correcta")
        try:
            logging.info("se comienza guardado del ticket")
            
            self.ejecutivoMesaController.crearTicket(ticket)
        except Exception as error:
            msg = "ocurrio un error al intengar guardar el ticket"
            logging.error(msg)
            logging.error(error)
            print(msg)    
    def formularioCreacionTicket(self):
        print 
        print("Creacion de Ticket")
        
        ticket = Ticket()
        
        ticket.nombreCliente = input("Ingrese Nombre Cliente: ")
        ticket.rutCliente = input("Ingrese Rut Cliente: ")
        ticket.telefono = input("Ingrese Telefono Cliente: ")
        ticket.detalle = input("Ingrese Detalle para el Ticket: ")
        
        return ticket
        
        