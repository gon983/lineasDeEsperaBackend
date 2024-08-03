
import random
import math



class Fin():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.proximoFin = 999


    def generarProximoFin(self, reloj):
        rnd = round(random.random(),4)
        tiempoAtencion = self.a + (self.b-self.a)* rnd
        self.proximoFin = round(reloj + tiempoAtencion,4)

        
    
    def vectorizar(self):
        return [self.proximoFin]
    
    def titularizar(self):
        return ["Proximo Fin"]
    



    def getProxFin(self):
        return self.proximoFin

    





class Llegada():
    def __init__(self, media, desviacion):
        self.media = media
        self.desviacion = desviacion
        self.primerRndUsado = False
        self.vRnd = []
        self.crearVrnd()
        self.proximaLlegada = 0
        self.generarProximaLlegada(0)

    def crearVrnd(self):
        v = []
        r1 = round(random.random(), 4)
        r2 = round(random.random(),4)
        v.append(r1)
        v.append(r2)
        self.vRnd = v

    def vectorizar(self):
        return [self.proximaLlegada]
    
    
    
    def titularizar(self):
        return ["Proxima llegada"]
    
    def getProxLlegada(self):
        return self.proximaLlegada


    def generarProximaLlegada(self, reloj):
        if self.primerRndUsado == False:
            self.primerRndUsado = True
            x1 = round((math.sqrt(-2 * math.log(self.vRnd[0], math.e)) * math.cos(2 * math.pi * self.vRnd[1])) * self.desviacion + self.media,4)
            tiempoEntreLlegadas = x1
            self.proximaLlegada = round(abs(tiempoEntreLlegadas) + reloj,4) #Agrego el absoluto porque no me pueden dar numeros negativos
            return x1
        
        else:
            x2 = round((math.sqrt(-2 * math.log(self.vRnd[0], math.e)) * math.sin(2 * math.pi * self.vRnd[1]))* self.desviacion + self.media,2) 
            self.crearVrnd()
            self.primerRndUsado = False
            tiempoEntreLlegadas = x2
            self.proximaLlegada = round(abs(tiempoEntreLlegadas) + reloj,4) #Agrego el absoluto porque no me pueden dar numeros negativos

            return x2  


    

    