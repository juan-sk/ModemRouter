from ast import While
from operator import truediv
from simple_term_menu import TerminalMenu
import os

def main():
    print("Bienvenido al software")
    main_menu_options = [
      "[A] Agregar",
      "[M] Modificar",
      "[E] Eliminar",
      "[C] Consultar",
      "[S] Salir",
    ]
    main_menu_show = True
    main_menu_terminal = TerminalMenu(main_menu_options)
    while main_menu_show:
      main_menu_index = main_menu_terminal.show()
      if main_menu_index == 0:
        print(f"La opción seleccionada fue {main_menu_options[main_menu_index]}!")
      elif main_menu_index == 1:
        print(f"La opción seleccionada fue {main_menu_options[main_menu_index]}!")
      elif main_menu_index == 2:
        print(f"La opción seleccionada fue {main_menu_options[main_menu_index]}!")
      elif main_menu_index == 3:
        print(f"La opción seleccionada fue {main_menu_options[main_menu_index]}!")
      elif main_menu_index == 4:
        main_menu_show = False
        print(f"La opción seleccionada fue {main_menu_options[main_menu_index]}!")
    print("Hasta luego")


if __name__ == "__main__":
    main()