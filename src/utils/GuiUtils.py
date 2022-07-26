import os
class GuiUtils:
    
    def __init__(self) -> None:
        self.widthWhitBars = 97
        self.totalWidth = 100
        pass

    @staticmethod
    def clearTerminal():
        os.system('cls' if os.name == 'nt' else 'clear')        
        
    @staticmethod
    def subrrayar(text):
      return   "\u0332".join(text)

    @staticmethod
    def customText(align, totalWidth, filler, text):
        if(type(text) != str):
            text = str(text)
        if align == 1:
            data = text.ljust(totalWidth, filler)
        elif align == 2:
            data = text.center(totalWidth, filler)            
        elif align == 3:
            data = text.rjsut(totalWidth, filler)
        else:
            data = text.center(totalWidth, filler)
        return data
    
    def customPrint(align, totalWidth, filler, text):
        if align == 1:
            data = text.ljust(totalWidth, filler)
        elif align == 2:
            data = text.center(totalWidth, filler)            
        elif align == 3:
            data = text.rjsut(totalWidth, filler)
        else:
            data = text.center(totalWidth, filler)
        print(data)

    @staticmethod
    def titulo(text):
        gui = GuiUtils()
        gui.separador()
        print("| " + text.center(gui.widthWhitBars) + "|")
        gui.separador()

    @staticmethod
    def tituloEspaciado(text):
        gui = GuiUtils()
        gui.separador()
        gui.espaciado()
        print("| " + text.center(gui.widthWhitBars) + "|")
        gui.espaciado()
        gui.separador()
    
    @staticmethod
    def subtitulo(text):
        gui = GuiUtils()
        print("| " + text.ljust(gui.widthWhitBars) + "|")
        gui.separador()
    
    @staticmethod
    def izq(text):
        gui = GuiUtils()
        print("| " + text.ljust(gui.widthWhitBars) + "|")
    
    @staticmethod
    def der(text):
        gui = GuiUtils()
        print("| " + text.ljust(gui.widthWhitBars) + "|")
    
    @staticmethod
    def separador():
        gui = GuiUtils()
        print("".center(gui.totalWidth, "-"))
    
    @staticmethod
    def espaciado():
        gui = GuiUtils()
        print("|" + GuiUtils.customText(2, 98, " ", " ") + "|")
        
    
    