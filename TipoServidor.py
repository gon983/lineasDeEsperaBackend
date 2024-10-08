from Servidor import *

class TipoServidor:
    
    def __init__(self, nombreTipo, cantidadServidores, a, b):
        self.nombreTipo = nombreTipo
        self.vTipoServidor = []
        for i in range(cantidadServidores):
            servidor = Servidor(i+1,a,b)
            self.vTipoServidor.append(servidor)
        self.cola = 0
        self.colaMax = 0

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
        numeroServidor = int(numeroServidor)
        for servidor in self.vTipoServidor:
            if servidor.getNumero() == numeroServidor:
                servidor.ocuparte(reloj)

    def liberarServidor(self, numeroServidor):
        for servidor in self.vTipoServidor:
            numeroServidor = int(numeroServidor)
            if servidor.getNumero() == numeroServidor:
                servidor.liberarte()
                break
        

    def getNombre(self):
        return self.nombreTipo
    
    def asignarACola(self):
        self.cola += 1
        if self.colaMax <= self.cola:
            self.colaMax = self.cola

    def sacarDeCola(self):
        self.cola -= 1

    def preguntarSiHayCola(self):
        if self.cola != 0:
            return True
        else:
            return False
        
    def getColaMaxima(self):
        return self.colaMax
    
    def getColas(self):
        return self.cola


