import logging
from utils.GuiUtils import GuiUtils 

class OpcionesComunes:
    
    @staticmethod
    def mostrarTipoTicket(tickets):
        GuiUtils.clearTerminal()
        GuiUtils.titulo("Jefe de mesa de ayuda")
        GuiUtils.subtitulo(" Listado de tipos de tickets existentes")
        header = "|" + GuiUtils.customText(2, 9, " ", "ID")
        header += "|" + GuiUtils.customText(2, 88, " ", "Nombre tipo de ticket") + "|"
        print(header)
        GuiUtils.separador()
        for item in tickets:
            #print("| %3s  | %30s | %30s |"%(item.id, item.nomArea, item.dscArea))
            data = "|" + GuiUtils.customText(2, 9, " ", item.id)
            data += "|" + GuiUtils.customText(2, 88, " ", item.nomTipoTicket) + "|"
            print(data)
            GuiUtils.separador()  

    @staticmethod
    def mostarUsuarios(usuarios):
        GuiUtils.clearTerminal()
        GuiUtils.titulo("Ejecutivo especifico")
        GuiUtils.subtitulo(" Listado de usuarios del sistema")        
        try:
            header = "|" + GuiUtils.customText(2, 9, " ", "ID")
            header += "|" + GuiUtils.customText(2, 28, " ", "Nombre")
            header += "|" + GuiUtils.customText(2, 23, " ", "Estado")
            header += "|" + GuiUtils.customText(2, 35, " ", "Tipo usuario") + "|"
            print(header)
            GuiUtils.separador()
            for item in usuarios:
                #printString  = "| %s  | %s    | %s    | %s     |"%(item.idTicket,item.nomCriticidad,item.nomTipoTicket,item.nombreCliente)
                data = "|" + GuiUtils.customText(2, 9, " ", item.id)
                data += "|" + GuiUtils.customText(2, 28, " ", item.nombreUsuario)
                data += "|" + GuiUtils.customText(2, 23, " ", item.dscEstado)
                data += "|" + GuiUtils.customText(2, 35, " ", item.dscTipoUsuario) + "|"    
                print(data)
            GuiUtils.separador()
        except Exception as error:
            logging.error("ocurrio un error al mostrar los tickets")
            logging.error(error)

    @staticmethod
    def presioneEnterContinuar():
        input(" Presione cualquier tecla continuar...")