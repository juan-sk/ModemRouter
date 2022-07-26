import logging
from gui.ejecutivoEspecifico.opciones.MostrarTicket import  MostrarTicket
from utils.GuiUtils import GuiUtils


class EjecutivoEspecifico:
    
    
    def __init__(self):
        self.mostrarTicket = MostrarTicket()
        pass
    
    def start(self,idUsuario):
        # print("inicio el menu de ejecutivo de mesa")
        self.menuOpciones(idUsuario)
        
    def menuOpciones(self,idUsuario):
        while True:
            opcion = self.opciones()
            if opcion == 1:
                self.mostrarTicket.start(idUsuario)
            elif opcion == 0:
                break
            
    def opciones(self):
        while True:
            try:
                GuiUtils.clearTerminal()
                GuiUtils.titulo("Ejecutivo especifico")
                GuiUtils.subtitulo("Menu de opciones ")
                GuiUtils.izq("1) Visualizar ticket")
                GuiUtils.izq("0) Cerrar sesión")
                GuiUtils.separador()
                opcionesValidas  = [1,0]
                value = int(input(" Ingrese un n° de opción para continuar: "))
                if value in opcionesValidas:
                    return value 
            except Exception as error:
                logging.error("ocurio un error en el menu de opciones de ejecutivo especifico")
                logging.error(error)
                print("ocurrio un error con la opcion que ingreso")