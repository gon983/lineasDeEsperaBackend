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
    
    def titularizar(self):
        v = []
        for servidor in self.vTipoServidor:
            vAux = servidor.titularizar(self.nombreTipo)
            v += vAux
        v+= ["cola " + self.nombreTipo]
        return v


    def getProxFin(self):
        v = []
        for servidor in self.vTipoServidor:
            proxFin = servidor.getProxFin()
            v.append(proxFin)
        tMin = min(v)
        for servidor in self.vTipoServidor:
            if servidor.getProxFin() == tMin:
                nombre_servidor = self.nombreTipo + "_" + str(servidor.getNumero())
                return tMin, nombre_servidor
            
    def tenesAlgunoLibre(self):
        for servidor in self.vTipoServidor:
            if servidor.estasLibre():
                return self.nombreTipo, servidor.getNumero()
        return False, False

    def asignarServidor(self, numeroServidor, reloj):
        for servidor in self.vTipoServidor:
            if servidor.getNumero() == numeroServidor and servidor.estasLibre():
                servidor.ocuparte(reloj)

    def getNombre(self):
        return self.nombreTipo


