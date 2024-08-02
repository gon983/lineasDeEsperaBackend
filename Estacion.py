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
    
    def obtenerProxFin(self):
        v = []
        nombreFin = "Fin_"
        tSurtidor, continuacionNombre = self.surtidores.getProximoFin()
        tGomeria, continuacionNombre =self.empleadosGomeria.getProximoFin()
        tAccesorios, continuacionNombre = self.empleadosVentaAccesorios.getProximoFin()
        v.append( self.surtidores.getProximoFin())
        v.append(self.empleadosGomeria.getProximoFin())
        v.append(self.empleadosVentaAccesorios.getProximoFin())
        min = min(v)
        if min == tSurtidor:
            nombreFin += continuacionNombre
            return tSurtidor, nombreFin
        elif min == tGomeria:
            nombreFin += continuacionNombre
            return tGomeria, continuacionNombre
        elif min == tAccesorios:
            nombreFin += continuacionNombre
            return tAccesorios, continuacionNombre
        else:
            print("Ha ocurrido un error de logica")



    
