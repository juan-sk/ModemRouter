import logging

from controller.EjecutivoMesaController import EjecutivoMesaController
from entity.TicketEntity import TicketEntity
from pojo.Ticket import Ticket
from utils.GuiUtils import GuiUtils


class CreaTicket:
    
    def __init__(self):
        self.ejecutivoMesaController = EjecutivoMesaController()
    
    
    def start(self,idUsuarioCreacion):
        ticket = self.formularioCreacionTicket(idUsuarioCreacion)
        print("se Ingresaron los datos del ticket de manera correcta")
        try:
            logging.info("se comienza guardado del ticket")
            
            self.ejecutivoMesaController.crearTicket(ticket)
            logging.info("se guardo correctamente el ticket")
        except Exception as error:
            msg = "ocurrio un error al intengar guardar el ticket"
            logging.error(msg)
            logging.error(error)
            print(msg)    
    def formularioCreacionTicket(self,idUsuarioCreacion):
        GuiUtils.clearTerminal()
        print("Creacion de Ticket")
        
        ticket = TicketEntity()
        
        ticket.nombreCliente = input("Ingrese Nombre Cliente: ")
        ticket.rutCliente = input("Ingrese Rut Cliente: ")
        ticket.telefono = input("Ingrese Telefono Cliente: ")
        ticket.detalle = input("Ingrese Detalle para el Ticket: ")
        ticket.idEstado = 1
        ticket.idUsuarioCreacion = idUsuarioCreacion
        ticket.idCriticidad = self.obtenerCriticidad()
        ticket.idArea  = self.obtenerArea()
        ticket.idTipoTicket = self.obenerTipoTicket()
        
        ticket.idUsuarioDerivado = self.obtenerUsuario(ticket.idArea)
        return ticket
    
    
    def obtenerCriticidad(self):
        criticidadSeleccionada = 0
        while True:
            GuiUtils.clearTerminal()
            print(GuiUtils.subrrayar("   Seleccione una Criticidad para el Ticket"))
            
            criticidades = self.ejecutivoMesaController.obtenerCriticidadesTicket();
            opcionesValidas=[]
            for item in criticidades:
                opcionesValidas.append(item.id)
                
                print("%d). %s"%(item.id,item.nomCriticidad))
            opcion = input(" Ingrese la Opcion") 
            opcionInt = 0
            try:
                opcionInt = int(opcion)
            except Exception :
                pass
            if opcionInt in opcionesValidas:
                criticidadSeleccionada = opcionInt
                break
                 
        return criticidadSeleccionada
        

    def obtenerArea(self):
        areaint = 0
        while True:
            GuiUtils.clearTerminal()
            print( GuiUtils.subrrayar( " Areas Disponibles"))
            
            areas =   self.ejecutivoMesaController.obtenerAreaTicket()
            opcionesValidas = []
            for item in areas:
                opcionesValidas.append(item.id)
                
                print("%d). %s"%(item.id,item.nomArea))
            opcion = input(" Ingrese la Opcion: ") 
            opcionInt = 0
            try:
                opcionInt = int(opcion)
            except Exception :
                pass
            if opcionInt in opcionesValidas:
                areaint = opcionInt
                break
        return areaint
    
    def obenerTipoTicket(self):
        tipoTicketInt = 0
        while True:
            GuiUtils.clearTerminal()
            print( GuiUtils.subrrayar( " Tipos de Tcket"))
            
            tipoTickets =   self.ejecutivoMesaController.obtenerTiposTickets()
            opcionesValidas = []
            for item in tipoTickets:
                opcionesValidas.append(item.id)
                
                print("%d). %s"%(item.id,item.nomTipoTicket))
            opcion = input(" Ingrese la Opcion: ") 
            opcionInt = 0
            try:
                opcionInt = int(opcion)
            except Exception :
                pass
            if opcionInt in opcionesValidas:
                tipoTicketInt = opcionInt
                break
        return tipoTicketInt
    def obtenerUsuario(self,idArea):
        usuarioDerivado = 0
        while True:
            GuiUtils.clearTerminal()
            print( GuiUtils.subrrayar( " Seleccione el usuario a Derivar Ticket"))
            
            usuarios =   self.ejecutivoMesaController.obtenerUsuarios(idArea)
            opcionesValidas = []
            for item in usuarios:
                opcionesValidas.append(item.id)
                
                print("%d). %s"%(item.id,item.nombreUsuario))
            opcion = input(" Ingrese la Opcion: ") 
            opcionInt = 0
            try:
                opcionInt = int(opcion)
            except Exception :
                pass
            if opcionInt in opcionesValidas:
                usuarioDerivado = opcionInt
                break
        return usuarioDerivado
            
                 
                   
        