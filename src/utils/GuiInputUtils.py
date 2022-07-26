import logging
from operator import ne



class GuiInputUtils:
    
    @staticmethod
    def inputTextCustom(opcionesValidas, text):
        while True:
            try:              
                value = int(input(text))
                if value in opcionesValidas:
                    return value 
            except Exception as error:
                logging.error("ocurio un error con el input ingresado")
                logging.error(error)
                print("ocurrio un error con el valor ingresado, Intente nuevamente ")
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
                value = input(" Confirma la operación [Si|No]: ")
                if(type(value) != str):
                    print("ingrese una opcion valida")
                else: 
                    value = value.upper()
                    if(value in opcionesValidas):
                        return value
            except Exception as error:
                logging.error("ocurio un error con el input ingresado")
                logging.error(error)
                print("ocurrio un error con el valor ingresado, Intente nuevamente ")
    @staticmethod
    def inputSiNo():
        resp = GuiInputUtils.inputString(["SI", "NO"])
        if resp == "SI":
            return 1
        else:
            return -1
        
        