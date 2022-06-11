import os
class GuiUtils:
    
    @staticmethod
    def clearTerminal():
        os.system('cls' if os.name == 'nt' else 'clear')