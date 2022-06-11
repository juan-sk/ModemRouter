import os
class GuiUtils:
    
    @staticmethod
    def clearTerminal():
        os.system('cls' if os.name == 'nt' else 'clear')
        
        
        
    @staticmethod
    def subrrayar(text):
      return   "\u0332".join(text)