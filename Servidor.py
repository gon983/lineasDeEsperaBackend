from Eventos import *

class Servidor:
    def __init__(self, numeroServidor, a, b):
        self.numeroServidor = numeroServidor
        self.estado = "libre"
        self.finAtencion = Fin(a,b)

    
    def vectorizar(self):
        v = [self.estado]
        v += self.finAtencion.vectorizar()
        return v
    
    def getProxFin(self):
        prox_fin = self.finAtencion.getProxFin()
        return prox_fin

    def getNumero(self):
        return self.numeroServidor
    
    def estasLibre(self):
        if self.estado == "libre":
            return True
        
    def ocuparte(self, reloj):
        self.estado = "ocupado"
        self.finAtencion.generarProximoFin(reloj)

