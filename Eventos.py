from abc import ABC, abstractmethod
import random
import math

class Evento(ABC):
    @abstractmethod
    def procesarEvento(self):
        pass

class Fin(Evento):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.rnd = ""
        self.tiempoAtencion = ""
        self.proximoFin = 999


    def generarProximoFin(self, reloj):
        self.rnd = round(random.random(),4)
        self.tiempoAtencion = self.a + (self.b-self.a)* self.rnd
        self.proximoFin = reloj + self.tiempoAtencion

        
    
    def vectorizar(self):
        return [self.rnd, self.proximoFin]
    
    def titularizar(self):
        return ["rnd", "Proximo Fin"]
    


    def procesarEvento(self):
        print(f"Llegada procesada a las {self.tiempo} desde {self.origen}")

    def getProxFin(self):
        return self.proximoFin

    





class Llegada(Evento):
    def __init__(self, media, desviacion):
        self.media = media
        self.desviacion = desviacion
        self.primerRndUsado = False
        self.vRnd = []
        self.crearVrnd()
        self.tiempoEntreLlegadas = self.generarProximaLlegada(0)
        self.proximaLlegada = self.tiempoEntreLlegadas

    def crearVrnd(self):
        v = []
        r1 = round(random.random(), 4)
        r2 = round(random.random(),4)
        v.append(r1)
        v.append(r2)
        self.vRnd = v

    def vectorizar(self):
        return [self.vRnd, self.proximaLlegada]
    
    
    
    def titularizar(self):
        return ["Par de rnd", "Proxima llegada"]
    
    def getProxLlegada(self):
        return self.proximaLlegada

    def procesarEvento(self):
        print(f"Fin procesado a las {self.tiempo} hacia {self.destino}")

    def generarProximaLlegada(self, reloj):
        if self.primerRndUsado == False:
            self.primerRndUsado = True
            x1 = round((math.sqrt(-2 * math.log(self.vRnd[0], math.e)) * math.cos(2 * math.pi * self.vRnd[1])) * self.desviacion + self.media,4)
            self.tiempoEntreLlegadas = x1
            self.proximaLlegada = self.tiempoEntreLlegadas + reloj
            return x1
        
        else:
            x2 = round((math.sqrt(-2 * math.log(self.vRnd[0], math.e)) * math.sin(2 * math.pi * self.vRnd[1]))* self.desviacion + self.media,2) 
            self.crearVrnd()
            self.primerRndUsado = False
            self.tiempoEntreLlegadas = x2
            self.proximaLlegada = self.tiempoEntreLlegadas + reloj

            return x2  


    

    