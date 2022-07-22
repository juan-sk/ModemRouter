import logging
from operator import ne



class GuiInputUtils:
    
    @staticmethod
    def inputNumber(opcionesValidas):
        while True:
            try:              
                # opcionesValidas  = [1,2,3]
                value = int(input("ingrese Opcion: "))
                if value in opcionesValidas:
                    return value 
                else: 
                    print("ingrese una opcion Valida")
            except Exception as error:
                logging.error("ocurio un error con el input ingresado")
                logging.error(error)
                print("ocurrio un error con el valor ingresado, Intente nuevamente ")
    @staticmethod
    def inputNumberNoParams():
        while True:
            try:              
                # opcionesValidas  = [1,2,3]
                value = int(input("ingrese Opcion: "))
                return value 
               
            except Exception as error:
                logging.error("ocurio un error con el input ingresado")
                logging.error(error)
                print("ocurrio un error con el valor ingresado, Intente nuevamente ")
    @staticmethod
    def inputString(opcionesValidas):
        while True:
            try:              
                # opcionesValidas  = [1,2,3]
                value = input("ingrese Opcion: ")
                if value in opcionesValidas:
                    return value 
                else: 
                    print("ingrese una opcion Valida")
            except Exception as error:
                logging.error("ocurio un error con el input ingresado")
                logging.error(error)
                print("ocurrio un error con el valor ingresado, Intente nuevamente ")
    @staticmethod
    def inputSiNo():
        afirmativos = ["si","Si","SI"];
        negativos = ["no","No","NO"]
        conbinado = afirmativos+negativos
        resp = GuiInputUtils.inputString(conbinado)
        if resp in afirmativos:
            return 1
        elif resp in negativos:
            return -1
        else:
            return 0
        
        