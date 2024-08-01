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
