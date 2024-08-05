from TipoServidor import *


class Estacion: 
    def __init__(self, cantidadSurtidores, cantidadEmpleadosGomeria, 
                cantidadEmpleadosVentaAccesorios, 
                aDuracionCargaCombustible, bDuracionCargaCombustible,
                aDuracionAtGomeria, bDuracionAtGomeria, 
                aDuracionVentaAccesorios, bDuracionVentaAccesorios):
        
        
        self.surtidores = TipoServidor("surtidor", cantidadSurtidores, aDuracionCargaCombustible, bDuracionCargaCombustible )
        self.empleadosGomeria = TipoServidor("gomeria", cantidadEmpleadosGomeria, aDuracionAtGomeria,  bDuracionAtGomeria )
        self.empleadosVentaAccesorios = TipoServidor("ventaAccesorios", cantidadEmpleadosVentaAccesorios, aDuracionVentaAccesorios, bDuracionVentaAccesorios)

    def vectorizarEstacion(self):
        x = self.surtidores.vectorizar() 
        y = self.empleadosGomeria.vectorizar()
        z = self.empleadosVentaAccesorios.vectorizar()
        return x + y + z
    
    def titularizarEstacion(self):
        x = self.surtidores.titularizar() 
        y = self.empleadosGomeria.titularizar()
        z = self.empleadosVentaAccesorios.titularizar()
        return x + y + z
    
    def tenesServidorDeEsteTipoLibre(self, nombreTipoServidor):
        nombreServidor, numero = False, False
        if nombreTipoServidor == self.surtidores.getNombre():
            nombreServidor, numero =  self.surtidores.tenesAlgunoLibre()
        elif nombreTipoServidor == self.empleadosGomeria.getNombre():
            nombreServidor, numero = self.surtidores.tenesAlgunoLibre()
        elif nombreTipoServidor == self.empleadosVentaAccesorios.getNombre():
            nombreServidor, numero = self.empleadosVentaAccesorios.tenesAlgunoLibre()
        else:
            print("Error en la parte de tenes servidor de este tipo libre")
        
        return nombreServidor, numero


    def obtenerProxFin(self):
        v = []
        tMin = 999
        nombreFin = "Fin_"
        tSurtidor, surtidor = self.surtidores.getProxFin()
        tGomeria, gomeria =self.empleadosGomeria.getProxFin()
        tAccesorios, accesorios= self.empleadosVentaAccesorios.getProxFin()
        v.append(tSurtidor)
        v.append(tGomeria)
        v.append(tAccesorios)
        tMin = min(v)
        if tMin == tSurtidor:
            nombreFin += surtidor
            return tSurtidor, nombreFin
        elif tMin == tGomeria:
            nombreFin += gomeria
            return tGomeria, nombreFin
        elif tMin == tAccesorios:
            nombreFin += accesorios
            return tAccesorios, nombreFin
        else:
            print("Ha ocurrido un error de logica")

    def asignarServidor(self, nombreTipoServidor, numeroServidor, reloj):
        if nombreTipoServidor == self.surtidores.getNombre():
            self.surtidores.asignarServidor(numeroServidor, reloj)
        elif nombreTipoServidor == self.empleadosGomeria.getNombre():
            self.surtidores.asignarServidor(numeroServidor, reloj)
        elif nombreTipoServidor == self.empleadosVentaAccesorios.getNombre():
            self.empleadosVentaAccesorios.asignarServidor(numeroServidor, reloj)
        else:
            print("El nombre del servidor no coincida con el pasado por parametro")

    def asignarACola(self, nombreTipoServidor):
        if nombreTipoServidor == self.surtidores.getNombre():
            self.surtidores.asignarACola()
        elif nombreTipoServidor == self.empleadosGomeria.getNombre():
            self.empleadosGomeria.asignarACola()
        elif nombreTipoServidor == self.empleadosVentaAccesorios.getNombre():
            self.empleadosVentaAccesorios.asignarACola()
        else:
            print("El nombre del servidor no coincida con el pasado por parametro")

    def preguntarSiHayColaParaElTipoDeServicio(self, nombreTipoServidor):
        if nombreTipoServidor == self.surtidores.getNombre():
            self.surtidores.preguntarSiHayCola()
        elif nombreTipoServidor == self.empleadosGomeria.getNombre():
            self.empleadosGomeria.preguntarSiHayCola()
        elif nombreTipoServidor == self.empleadosVentaAccesorios.getNombre():
            self.empleadosVentaAccesorios.preguntarSiHayCola()
        else:
            print("El nombre del servidor no coincida con el pasado por parametro")

    def sacarDeCola(self, nombreTipoServidor):
        if nombreTipoServidor == self.surtidores.getNombre():
            self.surtidores.sacarDeCola()
        elif nombreTipoServidor == self.empleadosGomeria.getNombre():
            self.empleadosGomeria.sacarDeCola()
        elif nombreTipoServidor == self.empleadosVentaAccesorios.getNombre():
            self.empleadosVentaAccesorios.sacarDeCola()
        else:
            print("El nombre del servidor no coincida con el pasado por parametro")

    def liberarServidor(self, nombreTipoServidor, numeroServidor):
        if nombreTipoServidor == self.surtidores.getNombre():
            self.surtidores.liberarServidor(numeroServidor)
        elif nombreTipoServidor == self.empleadosGomeria.getNombre():
            self.empleadosGomeria.liberarServidor(numeroServidor)
        elif nombreTipoServidor == self.empleadosVentaAccesorios.getNombre():
            self.empleadosVentaAccesorios.liberarServidor(numeroServidor)
        else:
            print("El nombre del servidor no coincida con el pasado por parametro")





    
