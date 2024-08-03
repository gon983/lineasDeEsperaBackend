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
        self.numeroIteracion = 0
        self.lineaInicioSimulacion = lineaInicioVisualizacion
        self.lineaFinSimulacion = lineaFinVisualizacion
        self.estacion = Estacion(cantidadSurtidores, cantidadEmpleadosGomeria, cantidadEmpleadosVentaAccesorios,
                                aDuracionCargaCombustible, bDuracionCargaCombustible,
                                aDuracionAtGomeria, bDuracionAtGomeria, 
                                aDuracionVentaAccesorios, bDuracionVentaAccesorios)
        self.clientes = Clientes(llegadaClientesMedia, llegadaClientesDesviacion) 
    

    def titularizar(self):
        # Primero van el reloj y el evento actual
        vFila = ["Reloj", "Evento"]
        # Despues va la llegada de clientes
        vFila += self.clientes.titularizarLlegada()
        # Despues va la Estacion...
        vFila += self.estacion.titularizarEstacion()
        return vFila

    def generarFila(self):
        # Primero van el reloj y el evento actual
        vFila = [self.reloj, self.eventoActual]
        # Despues va la llegada de clientes
        vFila += self.clientes.vectorizarLlegada()
        # Despues va la Estacion...
        vFila += self.estacion.vectorizarEstacion()
        # y finalmente los clientes
        vFila += self.clientes.vectorizarClientes() # ¿como hago para marcar los que van a "salir en la foto"? #lo voy a hacer con el nombre de los que llegan a su visualizacion
        return vFila


    
    def simular(self):
        tabla = []
        titulos = [self.titularizar()]
        tabla.append(titulos)
        for i in range(self.cantidadLineasASimular):
            self.numeroIteracion = i
            self.reloj, self.eventoActual = self.procesarEvento()
            if (i >= self.lineaInicioSimulacion and i <= self.lineaFinSimulacion) or (i == self.cantidadLineasASimular):
                fila = [self.generarFila()]
                tabla.append(fila)
                if i == 3:
                    break
            
        return {"simulacion": [tabla]}



    def procesarEvento(self): 
        relojA, nombreFin = self.estacion.obtenerProxFin()
        relojB , nombreLlegada= self.clientes.getProxLlegada()
        if relojA < relojB:
            self.procesarFin(relojA, nombreFin)
            return relojA, nombreFin
        else:
            self.procesarLlegada(relojB)
            return relojB, nombreLlegada

    
    def procesarFin(self, reloj , nombreFin):
        pass



    def procesarLlegada(self, reloj):
        self.clientes.generarProxLlegada(reloj)
        nombreTipoServidor = self.decidirServidor(0.8,0.08) #Aca se pueden cambiar las probabilidades-> primer argumento carga combustible, segundo gomeria y lo q sobra ventaAccesorios
        nombreServidor, numeroServidor = self.estacion.tenesServidorDeEsteTipoLibre(nombreTipoServidor) # retorna False, False si no encuentra el servidor
        if nombreServidor == False and numeroServidor == False: # Entonces no hay servidor libre
            pass
        elif isinstance(nombreServidor, str) and isinstance(numeroServidor, int): # Hay Servidor libre!
            self.estacion.asignarServidor(nombreServidor, numeroServidor, reloj)# asignar servidor incluye cambiarle el estado y generar cuando va a finalizar 
            esteClienteVaAserVisible = False
            if self.lineaInicioSimulacion <= self.numeroIteracion <= self.lineaFinSimulacion:
                esteClienteVaAserVisible = True
            self.clientes.crearClienteAtendido(nombreServidor, numeroServidor, reloj, esteClienteVaAserVisible) #recordar usar el booleano que maneja que los clientes que comienzan por combustible despues pueden ir a gomeria o a compra Accesorios tambien qie se necesita la hora de llegada para despues calcular tiempo de permanencia maximo en el sistema
        else:
            print("Error de logica en procesar llegada")

        

    
    def decidirServidor(self, cargarCombustible, gomeria):
        rnd = random.random()
        if rnd <= cargarCombustible:
            return "surtidor"
        elif rnd <= gomeria:
            return "gomeria"
        else:
            return "ventaAccesorios"
        
    


            
    
    
        




