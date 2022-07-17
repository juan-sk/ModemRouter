import logging
from controller.EjecutivoEspecificoController import EjecutivoEspecificoController
from controller.EjecutivoMesaController import EjecutivoMesaController
from controller.JefeDeMesaController import JefeDeMesaController
from repository.AreaRepository import AreaRepository
from repository.AreaUsuarioReposotory import AreaUsuarioReposotory
from repository.CriticidadRepository import CriticidadRepository
from repository.EstadoTicketRepository import EstadoTicketRepository
from repository.EstadoUsuarioRepository import EstadoUsuarioRepository
from repository.TicketRepository import TicketRepository
from repository.TipoTicketRepository import TipoTicketRepository
from repository.TipoUsuarioRepository import TipoUsuarioRepository
from repository.UsuarioRepository import UsuarioRepository
from service.TicketService import TicketService
from service.UsuarioService import UsuarioService


class ComponentConfig:
    @staticmethod
    def createComponents():
        logging.info("se crearan los Repositorios")
        ComponentConfig.createRepositories()
        ComponentConfig.createServices()
        ComponentConfig.createControllers()
        
    @staticmethod
    def createRepositories():
        AreaRepository.build()
        AreaUsuarioReposotory.build()
        CriticidadRepository.build()
        EstadoTicketRepository.build()
        EstadoUsuarioRepository.build()
        TicketRepository.build()
        TipoTicketRepository.build()
        TipoUsuarioRepository.build()
        UsuarioRepository.build()
    @staticmethod
    def createServices():
        TicketService.build()
        UsuarioService.build()
    @staticmethod
    def createControllers():
        EjecutivoEspecificoController.build()
        EjecutivoMesaController.build()
        JefeDeMesaController.build()
        UsuarioService.build()