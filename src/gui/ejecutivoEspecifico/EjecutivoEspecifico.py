import logging
from gui.ejecutivoEspecifico.opciones.MostrarTicket import  MostrarTicket
from utils.GuiUtils import GuiUtils


class EjecutivoEspecifico:
    
    
    def __init__(self):
        self.mostrarTicket = MostrarTicket()

        pass
    
    def start(self,idUsuario):
        print("inicio el menu de ejecutivo de mesa")
        GuiUtils.clearTerminal()
        self.menuOpciones(idUsuario)
        
    def menuOpciones(self,idUsuario):
        while True:
            opcion = self.opciones()
            if opcion == 1:
                self.mostrarTicket.start(idUsuario)
            elif opcion == 2:
                break

            
    def opciones(self):
        while True:
            try:
                GuiUtils.clearTerminal()
                print("     Ejecutivo Especifico         ")

                print (GuiUtils.subrrayar(" Opciones "))
                opcionesValidas  = [1,2]
                print("")
                print ("1). Visualizar ticket")
                print ("2). Cerrar Sesion")

                print ("")
                value = int(input("ingrese Opcion: "))
                if value in opcionesValidas:
                    # opcionMenu = value 
                    return value 
                else: 
                    print("ingrese una opcion Valida")
            except Exception as error:
                logging.error("ocurio un error en el menu de opciones de ejecutivo especifico")
                logging.error(error)
                print("ocurrio un error con la opcion que ingreso")