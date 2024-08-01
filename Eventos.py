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
        self.proximoFin = ""


    def generarProximoFin(self):
        self.rnd = random.random()
        self.proximoFin = self.a + (self.b-self.a)* self.rnd
        
    
    def vectorizar(self):
        return [self.rnd, self.proximoFin]
    


    def procesarEvento(self):
        print(f"Llegada procesada a las {self.tiempo} desde {self.origen}")

    





class Llegada(Evento):
    def __init__(self, media, desviacion):
        self.media = media
        self.desviacion = desviacion
        self.proximaLlegada = None
        self.primerRndUsado = False
        self.vRnd = []
        self.crearVrnd()
        self.generarProximaLlegada()

    def crearVrnd(self):
        v = []
        r1 = random.random()
        r2 = random.random()
        v.append(r1)
        v.append(r2)
        self.vRnd = v

    def vectorizar(self):
        return [self.vRnd , self.proximaLlegada]

    def procesarEvento(self):
        print(f"Fin procesado a las {self.tiempo} hacia {self.destino}")

    def generarProximaLlegada(self):
        if self.primerRndUsado == False:
            self.primerRndUsado = True
            return (math.sqrt(-2 * math.log(self.vRnd[0], math.e)) * math.cos(2 * math.pi * self.vRnd[1])) * self.desviacion + self.media
        
        else:
            x2 = (math.sqrt(-2 * math.log(self.vRnd[0], math.e)) * math.sin(2 * math.pi * self.vRnd[1]))* self.desviacion + self.media 
            self.crearVrnd()
            self.primerRndUsado = False

            return x2  


    

    