# from operator import truediv
from time import time
# from simple_term_menu import TerminalMenu
import os

import config.Config
import  config.DBConection 



class Application:
      
      def __init__(self):
        print("creando app")
        config.Config().configurar()
        print(self.config)
            
            
      def start(self):
        value = 0
        while True:
          print("la aplicacion inicio")
          time.sleep(5)  
          value = value+1
          if(value >=10):
            break   
          self.stop()
          
      def stop(self):
            config.DBConnection.close()
def main():
      
    App = Application()
    App.start()
    
    # print("Bienvenido al software")
    # main_menu_options = [
    #   "[A] Agregar",
    #   "[M] Modificar",
    #   "[E] Eliminar",
    #   "[C] Consultar",
    #   "[S] Salir",
    # ]
    # main_menu_show = True
    # main_menu_terminal = TerminalMenu(main_menu_options)
    # while main_menu_show:
    #   main_menu_index = main_menu_terminal.show()
    #   if main_menu_index == 0:
    #     print(f"La opción seleccionada fue {main_menu_options[main_menu_index]}!")
    #   elif main_menu_index == 1:
    #     print(f"La opción seleccionada fue {main_menu_options[main_menu_index]}!")
    #   elif main_menu_index == 2:
    #     print(f"La opción seleccionada fue {main_menu_options[main_menu_index]}!")
    #   elif main_menu_index == 3:
    #     print(f"La opción seleccionada fue {main_menu_options[main_menu_index]}!")
    #   elif main_menu_index == 4:
    #     main_menu_show = False
    #     print(f"La opción seleccionada fue {main_menu_options[main_menu_index]}!")
    # print("Hasta luego")


if __name__ == "__main__":
    main()