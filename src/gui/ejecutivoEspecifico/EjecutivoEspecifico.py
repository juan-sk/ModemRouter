import logging
from gui.ejecutivoEspecifico.VisualizarTicket import VisualizarTicket
from gui.ejecutivoEspecifico.AgregarObservacion import AgregarObservacion
from utils.GuiUtils import GuiUtils


class EjecutivoEspecifico:
    
    
    def __init__(self):
        self.visualizarTicket = VisualizarTicket()
        self.agregarObserbacion = AgregarObservacion()
        pass
    
    def start(self):
        print("inicio el menu de ejecutivo de mesa")
        GuiUtils.clearTerminal()
        self.menuOpciones()
        
    def menuOpciones(self):
        opcion = self.opciones()
        if opcion == 1:
            self.visualizarTicket.start()
        elif opcion == 2:
            self.agregarObserbacion.start()
            
    def opciones(self):
        while True:
            try:
                GuiUtils.clearTerminal()
                print("     Ejecutivo Especifico         ")

                print (GuiUtils.subrrayar(" Opciones "))
                opcionesValidas  = [1,2,3]
                print("")
                print ("1). Visualizar ticket")
                print ("2). Agregar observacion")
                print ("3). Cerrar ticket")
                print ("")
                value = int(input("Ingrese Opcion:"))
                if value in opcionesValidas:
                    # opcionMenu = value 
                    return value 
                else: 
                    print("ingrese una opcion Valida")
            except Exception as error:
                logging.error("ocurio un error en el menu de opciones de ejecutivo especifico")
                logging.error(error)
                print("ocurrio un error con la opcion que ingreso")