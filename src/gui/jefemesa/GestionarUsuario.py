import getpass
import logging
from controller.JefeDeMesaController import JefeDeMesaController
from entity.UsuarioEntity import UsuarioEntity
from pojo.Usuario import Usuario
from utils.GuiInputUtils import GuiInputUtils
from utils.GuiUtils import GuiUtils


class GestionarUsuario:
    
    def __init__(self ):
        self.jefeDeMesaController = JefeDeMesaController()

    

    def gestionarUsuario(self):
        opcionMenu = self.menuOpciones()
        if opcionMenu == 1:
            # ir a crear usuario
            print ("ir crear usuario")
            self.crearUsuario()
        elif opcionMenu == 2:
            #  ir a modificar usuario
            print ("ir modificar usuario")
        elif opcionMenu == 3:
            print ("ir a desactivar usuario")
                        
        return
    

    def menuOpciones(self):
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

    def crearUsuario(self):
        usuario = UsuarioEntity()
        while True:
            print("ingrese los datos del usuario")
            GuiUtils.clearTerminal()
            print("     Creacion de usuario         ")
            print("")
            usuario = self.formularioCreacionUsuario()
            print(usuario)
            
            print(" ¿Los valores para el Usuario son Correctos? (Si,No)")
            resp = GuiInputUtils.inputSiNo()
            if resp >0:
                break
            else:
                pass
            
        # guardar usuario
        resp =  self.jefeDeMesaController.guardarUsuario(usuario)
        if resp>0:
            print("el usuario fue creado Correctamente")
        else:
            print("Ocurrio Un error Al Crear El Usuario")
            
    
    def formularioCreacionUsuario(self):
        usuario = Usuario()
        nombreUsuario = input("Nombre de usuario:")
        print("Contraseña del usaurio")
        passwordUsuario =  getpass.getpass()
        
        print("Ingrese el tipo de usuario ")
        print("")
        print(GuiUtils.subrrayar(" Opciones "))
        # obrener opciones 
        tiposUsuario = self.jefeDeMesaController.obtenerTiposUsuario()
        opcionesValidas = []
        # imprimir opciones
        if len(tiposUsuario)>0:
            for item in tiposUsuario:
                print("%s). %s Descripcion:%s"%(item.id,item.nomTipoUsuario,item.dscTipoUsuraio))
                opcionesValidas.append(item.id)
                 
        idTipoUsuario = GuiInputUtils.inputNumber(opcionesValidas)
        
        idArea = 0
        if idTipoUsuario ==3:
            # agregar area 
            # obtener areas
            areas = self.jefeDeMesaController.obtenerAreas();
            # mostrar
            opcionesValidasArea = []
            if len(areas)>0:
                for item in areas:
                    print("%s). %s Detalle:%s"%(item.id,item.nomArea,item.dscArea))
                    opcionesValidasArea.append(item.id)
            idArea = GuiInputUtils.inputNumber(opcionesValidasArea)
        usuario.nombreUsuario = nombreUsuario
        usuario.password = passwordUsuario
        usuario.idEstado = 1
        usuario.idTipoUsuario =idTipoUsuario
        usuario.idArea = idArea
        return usuario
        
        
        
    
    @staticmethod
    def imprimirInfomracionUsuario(usuario,estado, tipoUsuario,area):
        print("Nombre:%s"%usuario.nombreUsuario)
        print("Password:%s"%usuario.password)
        print("Tipo Usuario:%s"%tipoUsuario)
        ejecutivoEspecialista =3
        if usuario.idTipoUsuario == ejecutivoEspecialista:
            print("Area Usuario:")
            
            
        
        