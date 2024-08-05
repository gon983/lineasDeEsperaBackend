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
    
    def titularizar(self, nombreTipo):
        v = ["estado " + str(nombreTipo) + " " + str(self.numeroServidor)]
        v += self.finAtencion.titularizar()
        return v
    
    def getProxFin(self):
        prox_fin = self.finAtencion.getProxFin()
        return prox_fin

    def getNumero(self):
        return self.numeroServidor
    
    def estasLibre(self):
        if self.estado == "libre":
            return True
        return False
        
    def estasOcupado(self):
        if self.estado == "ocupado":
            return True
        return False
        
    def ocuparte(self, reloj):
        self.estado = "ocupado"
        self.finAtencion.generarProximoFin(reloj)

    def liberarte(self):
        self.estado = "libre"
        self.finAtencion.setSinProximoFin()

