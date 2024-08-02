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
        tMin = 999
        nombreFin = "Fin_"
        tSurtidor, continuacionNombre = self.surtidores.getProxFin()
        tGomeria, continuacionNombre =self.empleadosGomeria.getProxFin()
        tAccesorios, continuacionNombre = self.empleadosVentaAccesorios.getProxFin()
        v.append(tSurtidor)
        v.append(tGomeria)
        v.append(tAccesorios)
        tMin = min(v)
        if tMin == tSurtidor:
            nombreFin += continuacionNombre
            return tSurtidor, nombreFin
        elif tMin == tGomeria:
            nombreFin += continuacionNombre
            return tGomeria, continuacionNombre
        elif tMin == tAccesorios:
            nombreFin += continuacionNombre
            return tAccesorios, continuacionNombre
        else:
            print("Ha ocurrido un error de logica")



    
