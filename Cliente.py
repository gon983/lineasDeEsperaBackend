
class Cliente:
    def __init__(self, id, estado, horaLlegada):
        self.id = id
        self.estado = estado
        self.horaLlegada = horaLlegada
        
        

    
    
    def getEstado(self):
        return self.estado
    
    def getNombre(self):
        return self.nombre
    
    def getId(self):
        return self.id
    
    def getHoraLlegada(self):
        return self.horaLlegada
    
    def serAtendido(self, tipoServidor, numeroServidor):
        self.estado = "C_"+ str(self.id) + "_"+ "SA_" + str(tipoServidor) + "_" + str(numeroServidor)

    def aCola(self, tipoServidor):
        self.estado = "C_"+ str(self.id) + "_" + "enCola_" + str(tipoServidor) + "_" + "0"


    