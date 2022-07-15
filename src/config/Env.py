from pathlib import Path
from dotenv import load_dotenv

class Env:
    
    
    def configs():
        try :
            print("cargando environment")
            dotenv_path = Path('../.config/.env')
            load_dotenv(dotenv_path=dotenv_path)

        except Exception:
            raise Exception("ocurrio un error para cargar el archivo .env")
