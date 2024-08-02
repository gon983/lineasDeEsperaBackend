from Eventos import *

class Clientes:
    def __init__(self, media, desviacion):
        self.vClientes = []
        self.proximaLlegada = Llegada(media,  desviacion)

    def vectorizarLlegada(self):
        return self.proximaLlegada.vectorizar()
    
    def getProxLlegada(self):
        return self.proximaLlegada.getProxLlegada()
