import logging
from service.TicketService import TicketService
from service.UsuarioService import UsuarioService


class JefeDeMesaController:
    
        
    def __init__(self) :

        self.usuarioService = UsuarioService._usuarioService
        self.ticketService = TicketService._ticketService
    def guardarArea(self,areaEntity):
        return self.ticketService.guardarArea(areaEntity)
        
    def obtenerTiposUsuario(self):
        try:
            logging.info("se inicia la obtencion de tipos de usuario")
            tiposUsuario=  self.usuarioService.obtenerTiposDeUsuario()
            logging.info("se termina la obtencion de tipos de usuario")
            return tiposUsuario
        except Exception as error:
            logging.error(error)
            # se retorna null 
            pass
    def obtenerAreas(self):
        try:
            
            areas = self.usuarioService.obtenerArea()
            return areas
        except Exception as error:
            logging.error("ocurrio un error al obtener las areas")
            logging.error(error)
    def guardarUsuario(self,usuario):
        try:
            self.usuarioService.guardarUsuario(usuario)
            return 1
        except Exception as error :
            logging.error("ocurrio un error guardando el usuario")
            logging.error (error)
            return -1
        
    def obtenerUsuarios(self):
        try:
            usuarios = self.usuarioService.obtenerUusarios();
          
            return usuarios
        except Exception as error:
            logging.error("ocurrio un error obteniendo usuarios")
            logging.error(error)
            pass
        
    def desactivarUusario(self, isUsuario):
        try:
            usuarios = self.usuarioService.desactivarUsuario(isUsuario);
          
            return usuarios
        except Exception as error:
            logging.error("ocurrio un error obteniendo usuarios")
            logging.error(error)
            pass
    def obtenerAreas(self):
        return self.ticketService.obtenerAreas()
    def validarRelacionArea(self, idAreaAValidar):
        return self.ticketService.validarRelacionArea(idAreaAValidar)
    def eliminarArea(self,idAreaEliminar):
        return self.ticketService.eliminarArea(idAreaEliminar)
    
    
    
    def guardarTipoTicket(self,tipoTicket):
        return self.ticketService.guardarTipoTicket(tipoTicket)
    def  obtenerTiposTicket(self):
        return self.ticketService.obtenerTiposTickets()
    def modificarTipoTicket(self, tipoTicket):
        return self.ticketService.modificarTipoTicket(tipoTicket)
    def eliminarTipoTicket(self, idTipoTicketEliminar):
        return self.ticketService.eliminarTipoTicket(idTipoTicketEliminar)
    def tipoTicketEliminable(self, idTipoTicketElimnar):
        return self.ticketService.tipoTicketElimnable(idTipoTicketElimnar)
    def tipoTicketElimnable(self, idTipoTicketElimnar):
        
       return self.ticketService.tipoTicketElimnable(idTipoTicketElimnar)

    @staticmethod
    def build():
        JefeDeMesaController._jefeDeMesaController = JefeDeMesaController()