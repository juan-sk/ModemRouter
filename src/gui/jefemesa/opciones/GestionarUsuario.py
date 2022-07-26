import getpass
import logging
from controller.JefeDeMesaController import JefeDeMesaController
from entity.UsuarioEntity import UsuarioEntity
from gui.OpcioensComunes import OpcionesComunes
from pojo.Usuario import Usuario
from utils.GuiInputUtils import GuiInputUtils
from utils.GuiUtils import GuiUtils


class GestionarUsuario:
    
    def __init__(self ):
        self.jefeDeMesaController = JefeDeMesaController._jefeDeMesaController

    

    def start(self):
        while True:
            
            #opcionMenu = self.menuOpciones()
            opcionMenu = 2
            if opcionMenu == 1:
                # ir a crear usuario
                # print ("ir crear usuario")
                self.crearUsuario()
            elif opcionMenu == 2:
                #  ir a modificar usuario
                self.modificarUsuario()
            elif opcionMenu == 3:
                
                # print ("ir a desactivar usuario")
                self.desactivarUsuario()
            elif opcionMenu == 0:
                break
            return
    

    def menuOpciones(self):
        GuiUtils.clearTerminal()
        GuiUtils.titulo("Jefe de mesa de ayuda")
        GuiUtils.subtitulo("Menu de opciones para usuario")
        GuiUtils.izq("1) Crear usuario")
        GuiUtils.izq("2) Modificar usuario")
        GuiUtils.izq("3) Activar o desactivar usuarios")
        GuiUtils.izq("0) Volver")
        GuiUtils.separador()
        opcionesValidas = [0,1,2,3]
        value = int(input(" Ingrese un n° de opción para continuar: "))
        if value in opcionesValidas:
            return value

    def crearUsuario(self):
        while True:
            usuario = UsuarioEntity()
            GuiUtils.clearTerminal()
            GuiUtils.titulo("Jefe de mesa de ayuda")
            GuiUtils.subtitulo(" Creación de usuario")
            GuiUtils.subtitulo(" Por favor ingrese el detalle requerido: ")
            nombreUsuario = input(" Nombre de usuario: ")
            nombreUsuarioDisponible = self.jefeDeMesaController.nombreUsuarioDisponible(nombreUsuario)
            if(nombreUsuarioDisponible): 
                usuario = self.formularioCreacionUsuario(nombreUsuario)
                GuiUtils.clearTerminal()
                GuiUtils.titulo("Jefe de mesa de ayuda")
                GuiUtils.subtitulo(" Creación de usuario")
                GuiUtils.subtitulo(" Vista previa del usuario: ")
                data = "|" + GuiUtils.customText(2, 49, " ", "Nombre de usuario: ")
                data += "|" + GuiUtils.customText(2, 48, " ", usuario.nombreUsuario) + "|"
                print(data)
                data = "|" + GuiUtils.customText(2, 49, " ", "Contraseña: ")
                data += "|" + GuiUtils.customText(2, 48, " ", usuario.password) + "|"
                print(data)
                data = "|" + GuiUtils.customText(2, 49, " ", "Tipo de usuario: ")
                data += "|" + GuiUtils.customText(2, 48, " ", usuario.dscTipoUsuario) + "|"
                print(data)
                data = "|" + GuiUtils.customText(2, 49, " ", "Área: ")
                data += "|" + GuiUtils.customText(2, 48, " ", usuario.dscArea) + "|"
                print(data)
                GuiUtils.separador()
                resp = GuiInputUtils.inputSiNo()
                if resp < 0:
                    break
                else:    
                    resp =  self.jefeDeMesaController.guardarUsuario(usuario)
                    GuiUtils.clearTerminal()
                    GuiUtils.tituloEspaciado("Usuario creado correctamente")
                    input(" Presione cualquier tecla continuar...")
                    break
            else:
                GuiUtils.clearTerminal()
                GuiUtils.tituloEspaciado("El usuario [" + nombreUsuario + "], ya existe")
                GuiUtils.espaciado()
                GuiUtils.izq("1) Ingresar un nuevo usuario")
                GuiUtils.izq("0) Volver")
                GuiUtils.espaciado()
                GuiUtils.separador()
                opcionesValidas  = [0, 1]
                text = " Ingrese un n° de opción para continuar: "
                value = GuiInputUtils.inputTextCustom(opcionesValidas, text)
                if(value == 0):
                    break
    
    def formularioCreacionUsuario(self, nombreUsuarioDisponible):
        usuario = Usuario()
        nombreUsuario = nombreUsuarioDisponible
        passwordUsuario =  getpass.getpass(" Contraseña: ")
        GuiUtils.separador()            
        GuiUtils.subtitulo(" Tipo de usuario: ")
        tiposUsuario = self.jefeDeMesaController.obtenerTiposUsuario()
        opcionesValidas = []
        # if len(tiposUsuario) >0:
        for item in tiposUsuario:
            opcionesValidas.append(item.id)
            #print("%s). %s - Descripcion:%s"%(item.id,item.nomTipoUsuario,item.dscTipoUsuraio))
            GuiUtils.izq("%s). %s: %s"%(item.id,item.nomTipoUsuario,item.dscTipoUsuraio))
        GuiUtils.separador()           
        text = " Seleccione una opción: "
        idTipoUsuario = GuiInputUtils.inputTextCustom(opcionesValidas, text)
        usuario.dscTipoUsuario = Usuario.encontrarTipoUsuario(idTipoUsuario,tiposUsuario).nomTipoUsuario
        idArea = 0
        usuario.dscArea = "No asignada"
        if idTipoUsuario == 3:
            # agregar area 
            # obtener areas
            areas = self.jefeDeMesaController.obtenerAreas()
            # mostrar
            opcionesValidasArea = []
            #if len(areas)>0:
            GuiUtils.separador()           
            for item in areas:
                opcionesValidasArea.append(item.id)
                #print("%s) %s Detalle:%s"%(item.id,item.nomArea,item.dscArea))
                GuiUtils.izq("%s) %s Detalle:%s"%(item.id,item.nomArea,item.dscArea))
            GuiUtils.separador()           
            text = " Seleccione una opción: "
            idArea = GuiInputUtils.inputTextCustom(opcionesValidasArea, text)
            for item in areas:
                if(item.id == idArea):
                    usuario.dscArea = item.nomArea
        usuario.nombreUsuario = nombreUsuario
        usuario.password = passwordUsuario
        usuario.idEstado = 1
        usuario.idTipoUsuario =idTipoUsuario
        usuario.idArea = idArea
        return usuario
        
    def modificarUsuario(self):
        while True:
            usuarios = self.jefeDeMesaController.obtenerUsuarios()
            OpcionesComunes.mostarUsuarios(usuarios)
            opcionesValidas = []
            for item in usuarios:
                opcionesValidas.append(item.id)

            opcionSalida = 0
            opcionesValidas.append(opcionSalida)
        
            text = " Ingresar n° de usuario a modificar (ingrese 0 volver atras): "
            idUsuario = GuiInputUtils.inputTextCustom(opcionesValidas, text)
            
            if idUsuario == 0:
                break
            else:
                for item in usuarios:
                    if(item.id == idUsuario):
                        usuario = item
                GuiUtils.clearTerminal()
                GuiUtils.titulo("Ejecutivo mesa de ayuda")
                GuiUtils.subtitulo(" modificación de usuario: " + usuario.nombreUsuario)
                GuiUtils.subtitulo(" Por favor ingrese el detalle requerido: ")
                usuario.password =  getpass.getpass(" Contraseña: ")
                self.jefeDeMesaController.modificarUsuario(usuario)
                GuiUtils.clearTerminal()
                GuiUtils.tituloEspaciado("Usuario modificado correctamente")
                input(" Presione cualquier tecla continuar...")

    
    @staticmethod
    def imprimirInfomracionUsuario(usuario,estado, tipoUsuario,area):
        print("Nombre:%s"%usuario.nombreUsuario)
        print("Password:%s"%usuario.password)
        print("Tipo Usuario:%s"%tipoUsuario)
        ejecutivoEspecialista =3
        if usuario.idTipoUsuario == ejecutivoEspecialista:
            print("Area Usuario:")
            
            
  
    def desactivarUsuario(self):
        while True:
            usuarios = self.jefeDeMesaController.obtenerUsuarios()
            OpcionesComunes.mostarUsuarios(usuarios)
            opcionesValidas = []
            for item in usuarios:
                opcionesValidas.append(item.id)

            opcionSalida = 0
            opcionesValidas.append(opcionSalida)

            text = " Ingresar n° del usuario al cual se cambiara su estado (ingrese 0 volver atras): "
            idUsuario = GuiInputUtils.inputTextCustom(opcionesValidas, text)
            
            if idUsuario == 0:
                break
            else:    
                for item in usuarios:
                    if(item.id == idUsuario):
                        usuario = item
                resultado = self.jefeDeMesaController.desactivarUusario(usuario)
                text = "Usuario " + resultado + " correctamente"
                GuiUtils.clearTerminal()
                GuiUtils.tituloEspaciado(text)
                input(" Presione cualquier tecla continuar...")
                break
        