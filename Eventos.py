from abc import ABC, abstractmethod

class Evento(ABC):
    @abstractmethod
    def procesar(self):
        pass

class Llegada(Evento):
    def __init__(self):
        pass

    def procesar(self):
        print(f"Llegada procesada a las {self.tiempo} desde {self.origen}")

class Fin(Evento):
    def __init__(self):
        pass

    def procesar(self):
        print(f"Fin procesado a las {self.tiempo} hacia {self.destino}")