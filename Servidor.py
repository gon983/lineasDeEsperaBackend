from Eventos import *

class Servidor:
    def __init__(self, numeroServidor, a, b):
        self.numeroServidor = numeroServidor
        self.estado = "libre"
        self.finAtencion = Fin(a,b)
