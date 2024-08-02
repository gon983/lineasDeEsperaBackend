from Servidor import *

class TipoServidor:
    
    def __init__(self, nombreTipo, cantidadServidores, a, b):
        self.nombreTipo = nombreTipo
        self.vTipoServidor = []
        for i in range(cantidadServidores):
            servidor = Servidor(i+1,a,b)
            self.vTipoServidor.append(servidor)
        self.cola = 0

    def vectorizar(self):
        v = []
        for servidor in self.vTipoServidor:
            vAux = servidor.vectorizar()
            v += vAux
        v += [self.cola]
        return v
    
    def getProxFin(self):
        v = []
        for servidor in self.vTipoServidor:
            v.append(servidor.getProxFin())
        tMin = min(v)
        for servidor in self.vTipoServidor:
            if servidor.getProxFin() == tMin:
                nombre_servidor = self.nombreTipo + "_" + servidor.getNumero()
                return tMin


