from time import time

from config.Config import Config
from config.DBConection import DBConnection



class Application:
      
      def __init__(self):
        Config().configurar()
            
      def start(self):
        value = 0
        while True:
          print("la aplicacion inicio")
          # time.sleep(5)  
          value = value+1
          print(value)
          if(value >=10):
            break   
        self.stop()
          
      def stop(self):
            DBConnection.close()
            
            
  
def main():
    
    App = Application()
    App.start()
  


if __name__ == "__main__":
    main()