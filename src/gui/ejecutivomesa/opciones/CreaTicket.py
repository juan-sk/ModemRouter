import logging

from controller.EjecutivoMesaController import EjecutivoMesaController
from entity.TicketEntity import TicketEntity
from pojo.Ticket import Ticket
from utils.GuiUtils import GuiUtils


class CreaTicket:
    
    def __init__(self):
        self.ejecutivoMesaController = EjecutivoMesaController._ejecutivoMesaController
        
    def start(self,idUsuarioCreacion):
        ticket = self.formularioCreacionTicket(idUsuarioCreacion)
        try:
            logging.info("se comienza guardado del ticket")
            self.ejecutivoMesaController.crearTicket(ticket)
            logging.info("se guardo correctamente el ticket")
            GuiUtils.clearTerminal()
            GuiUtils.tituloEspaciado("Ticket creado correctamente")
            input(" Presione cualquier tecla continuar...")

        except Exception as error:
            msg = "ocurrio un error al intengar guardar el ticket"
            logging.error(msg)
            logging.error(error)
            print(msg) 

    def formularioCreacionTicket(self,idUsuarioCreacion):
        ticket = TicketEntity()
        GuiUtils.clearTerminal()
        GuiUtils.titulo("Ejecutivo mesa de ayuda")
        GuiUtils.subtitulo(" Creación de ticket")
        GuiUtils.subtitulo(" Por favor ingrese el detalle requerido: ")
        ticket.nombreCliente = input(" Cliente: ")
        ticket.rutCliente = input(" Rut: ")
        ticket.telefono = input(" Telefono: ")
        ticket.correoElectronico = input(" Correo eletrónico: ")
        ticket.detalle = input(" Detalle de ticket: ")
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
            GuiUtils.separador()            
            GuiUtils.subtitulo(" Criticidad del ticket: ")
            criticidades = self.ejecutivoMesaController.obtenerCriticidadesTicket();
            opcionesValidas=[]
            for item in criticidades:
                opcionesValidas.append(item.id)
                #print("%d %s"%(item.id,item.nomCriticidad))
                GuiUtils.izq("%d) %s"%(item.id,item.nomCriticidad))
            GuiUtils.separador()            
            opcion = input(" Seleccione una opción: ") 
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
            GuiUtils.separador()            
            GuiUtils.subtitulo(" Área del ticket: ")
            
            areas =   self.ejecutivoMesaController.obtenerAreaTicket()
            opcionesValidas = []
            for item in areas:
                opcionesValidas.append(item.id)
                #print("%d %s"%(item.id,item.nomArea))
                GuiUtils.izq("%d) %s"%(item.id,item.nomArea))
            GuiUtils.separador()            
            opcion = input(" Seleccione una opción: ") 
            
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
            GuiUtils.separador()            
            GuiUtils.subtitulo(" Tipo de ticket: ")
            
            tipoTickets =   self.ejecutivoMesaController.obtenerTiposTickets()
            opcionesValidas = []
            for item in tipoTickets:
                opcionesValidas.append(item.id)
                #print("%d) %s"%(item.id,item.nomTipoTicket))
                GuiUtils.izq("%d) %s"%(item.id,item.nomTipoTicket))
            GuiUtils.separador()            
            opcion = input(" Seleccione una opción: ") 
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
            GuiUtils.separador()            
            GuiUtils.subtitulo(" Usuario especialista a derivar el ticket: ")
            usuarios =   self.ejecutivoMesaController.obtenerUsuarios(idArea)
            opcionesValidas = []
            for item in usuarios:
                opcionesValidas.append(item.id)
                #print("%d) %s"%(item.id,item.nombreUsuario))
                GuiUtils.izq("%d) %s"%(item.id,item.nombreUsuario))
            GuiUtils.separador()            
            opcion = input(" Seleccione una opción: ") 
            opcionInt = 0
            try:
                opcionInt = int(opcion)
            except Exception :
                pass
            if opcionInt in opcionesValidas:
                usuarioDerivado = opcionInt
                break
        return usuarioDerivado         
                   
        