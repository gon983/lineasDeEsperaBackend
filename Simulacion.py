from  Estacion import *
from Clientes import *

class Simulacion:

    def __init__(self, cantidadLineasASimular, duracionSimulacion, lineaInicioVisualizacion,
            lineaFinVisualizacion, cantidadSurtidores, cantidadEmpleadosGomeria, cantidadEmpleadosVentaAccesorios,
            llegadaClientesMedia, llegadaClientesDesviacion, aDuracionCargaCombustible, bDuracionCargaCombustible,
            aDuracionAtGomeria, bDuracionAtGomeria, aDuracionVentaAccesorios, bDuracionVentaAccesorios):
        
        self.reloj = 0
        self.eventoActual = "Inicializacion"
        self.cantidadLineasASimular = cantidadLineasASimular
        self.duracionSimulacion = duracionSimulacion
        self.lineaInicioSimulacion = lineaInicioVisualizacion
        self.lineaFinSimulacion = lineaFinVisualizacion
        self.estacion = Estacion(cantidadSurtidores, cantidadEmpleadosGomeria, cantidadEmpleadosVentaAccesorios,
                                aDuracionCargaCombustible, bDuracionCargaCombustible,
                                aDuracionAtGomeria, bDuracionAtGomeria, 
                                aDuracionVentaAccesorios, bDuracionVentaAccesorios)
        self.clientes = Clientes(llegadaClientesMedia, llegadaClientesDesviacion) 
    


    def generarFila(self):
        # Primero van el reloj y el evento actual
        vFila = [self.reloj, self.eventoActual]
        # Despues va la llegada de clientes
        vFila += self.clientes.vectorizarLlegada()
        # Despues va la Estacion...
        vFila += self.estacion.vectorizarEstacion()
        return vFila


    def generarTabla(self):
        fila = self.generarFila()
        return { "simulacion": [fila]}
    
    def simular(self):
        tabla = []
        for i in range(self.cantidadLineasASimular):
            if (i >= self.lineaInicioSimulacion and i <= self.lineaFinSimulacion) or (i == self.cantidadLineasASimular):
                tabla.append(fila)
                fila = [self.generarFila()]
                if i == 2:
                    break
            self.reloj, self.eventoActual = self.procesarEvento()
        return {"simulacion": [tabla]}



    def procesarEvento(self): #Aca deberia haber una interfaz ??? Tendria q hacer todo de vuelta
        relojA, nombreFin = self.estacion.obtenerProxFin()
        relojB , nombreLlegada= self.clientes.getProxLlegada()
        if relojA > relojB:
            self.procesarFin(relojA, nombreFin)
            return relojA, nombreFin
        else:
            self.procesarLlegada(relojB, nombreLlegada)
            return relojB, nombreLlegada

    
    def procesarFin(self, reloj , nombreFin):
        pass



    def procesarLlegada(self, reloj):
        self.clientes.generarProxLlegada(reloj)
        nombreTipoServidor = self.decidirServidor(cargarCombustible=0.8,gomeria=0.08) #Aca se pueden cambiar las probabilidades
        nombreServidor, numeroServidor = self.estacion.tenesServidorDeEsteTipoLibre(nombreTipoServidor) # retorna False, False si no encuentra el servidor
        if nombreServidor == False and numeroServidor == False: # Entonces no hay servidor libre
            pass
        else: # Hay Servidor libre!
            self.estacion.asignarServidor(nombreServidor, numeroServidor, reloj) # asignar servidor incluye cambiarle el estado y generar cuando va a finalizar
            self.clientes.crearClienteAtendido(nombreServidor, numeroServidor)

        

    
    def decidirServidor(cargarCombustible, gomeria):
        rnd = random.random()
        if rnd <= cargarCombustible:
            return "surtidor"
        elif rnd <= gomeria:
            return "gomeria"
        else:
            return "ventaAccesorios"
        
    


            
    
    
        




