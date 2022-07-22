
class OpcionesComunes:
    
    @staticmethod
    def mostrarTipoTicket( tickets):
        HEADER = "|  ID  |   Nombre Tipo Ticket     |   Decripcion Tipo Ticket"
        print(HEADER)
        for item in tickets:
            row = "|  %3s | %20s | %20s|"%(item.id,item.nomTipoTicket,item.dscTipoTicket)
            print(row)
    
    @staticmethod
    def mostarUsuarios( usuarios):
        HEADER = "|  ID  |        Nombre         |  Estado |     Tipo Usuario    |"

        print(HEADER)
        for us in usuarios:
            print("| %3s  |  %20s | %s | %13s |"%(us.id,us.nombreUsuario,us.dscEstado,us.dscTipoUsuario))
    @staticmethod
    def presioneEnterContinuar():
        input("Presione Enter para Continuar")