import logging
from utils.GuiUtils import GuiUtils


class GestionarUsuario:
    
    def __init__(self ):
        pass
    
    
    @staticmethod
    def gestionarUsuario():
        opcionMenu = GestionarUsuario.menuOpciones()
        if opcionMenu == 1:
            # ir a crear usuario
            print ("ir crear usuario")
            GestionarUsuario.crearUsuario()
        elif opcionMenu == 2:
            #  ir a modificar usuario
            print ("ir modificar usuario")
        elif opcionMenu == 3:
            print ("ir a desactivar usuario")
                        
        return
    

    @staticmethod
    def menuOpciones():
        while True:
            try:
                GuiUtils.clearTerminal()
                print("     Gestion de usuario         ")

                print (GuiUtils.subrrayar(" Opciones "))
                opcionesValidas  = [1,2,3]
                print("")
                print ("1). Crea Usuario")
                print ("2). Modifica Usuario")
                print ("3). Desactiva Usuario")
                print ("")
                value = int(input("Ingrese Opcion:"))
                if value in opcionesValidas:
                    # opcionMenu = value 
                    return value 
                else: 
                    print("ingrese una opcion Valida")
            except Exception as error:
                logging.error("ocurio un error en el menu de opciones de gestion de usuario")
                logging.error(error)
                print("ocurrio un error con la opcion que ingreso")
    @staticmethod
    def crearUsuario():
        GuiUtils.clearTerminal()
        print("     Creacion de usuario         ")
    
    @staticmethod
    def imprimirInfomracionUsuario(usuario):
        print("nombre:%s"%usuario.nombreUsuario)
        print
        
        