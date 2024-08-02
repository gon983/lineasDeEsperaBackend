from TipoServidor import *


class Estacion: 
    def __init__(self, cantidadSurtidores, cantidadEmpleadosGomeria, 
                cantidadEmpleadosVentaAccesorios, 
                aDuracionCargaCombustible, bDuracionCargaCombustible,
                aDuracionAtGomeria, bDuracionAtGomeria, 
                aDuracionVentaAccesorios, bDuracionVentaAccesorios):
        
        
        self.surtidores = TipoServidor("surtidor", cantidadSurtidores, aDuracionCargaCombustible, bDuracionCargaCombustible )
        self.empleadosGomeria = TipoServidor("empleado gomeria", cantidadEmpleadosGomeria, aDuracionAtGomeria,  bDuracionAtGomeria )
        self.empleadosVentaAccesorios = TipoServidor("e. venta accesorios", cantidadEmpleadosVentaAccesorios, aDuracionVentaAccesorios, bDuracionVentaAccesorios)

    def vectorizarEstacion(self):
        x = self.surtidores.vectorizar() 
        y = self.empleadosGomeria.vectorizar()
        z = self.empleadosVentaAccesorios.vectorizar()
        return x + y + z
    
    def obtenerProximoEvento(self):
        v = []
        tSurtidor = self.surtidores.getProximoFin()
        tGomeria =self.empleadosGomeria.getProximoFin()
        tAccesorios = self.empleadosVentaAccesorios.getProximoFin()
        v.append( self.surtidores.getProximoFin())
        v.append(self.empleadosGomeria.getProximoFin())
        v.append(self.empleadosVentaAccesorios.getProximoFin())
        min = min(v)
        if min == tSurtidor:
            return tSurtidor
        elif min == tGomeria:
            return tGomeria
        elif min == tAccesorios:
            return tAccesorios
        else:
            print("Ha ocurrido un error de logica")



    
