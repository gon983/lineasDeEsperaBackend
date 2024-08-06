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
        self.maxTCliente = 0
        self.colasMaximas = [0,0,0]
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
        # Despues las colas maximas
        vFila += ["Max Cola surtidor", "Max Cola Gomeria", "Max Cola venta accesorios"]
        vFila += ["Max T Cliente"]
        return vFila

    def generarFila(self):
        # Primero van el reloj y el evento actual
        vFila = [self.reloj, self.eventoActual]
        # Despues va la llegada de clientes
        vFila += self.clientes.vectorizarLlegada()
        # Despues va la Estacion...
        vFila += self.estacion.vectorizarEstacion()
        # Dspues las colas maximas y el t max de un cliente
        print(self.colasMaximas)
        vFila += self.colasMaximas
        vFila += [self.maxTcliente]
        # y finalmente los clientes
        vFila += self.clientes.vectorizarClientes() # ¿como hago para marcar los que van a "salir en la foto"? #lo voy a hacer con el nombre de los que llegan a su visualizacion
        return vFila


    
    def simular(self):
        tabla = []
        titulos = [self.titularizar()]
        tabla.append(titulos)
        for i in range(self.cantidadLineasASimular):
            
            self.reloj, self.eventoActual = self.procesarEvento()
            self.colasMaximas = self.estacion.getColasMaximas(self.colasMaximas)
            self.maxTcliente = self.clientes.getMaxTCliente()
            if (i >= self.lineaInicioSimulacion and i <= self.lineaFinSimulacion) or (i == self.cantidadLineasASimular - 1):
                fila = [self.generarFila()]
                tabla.append(fila)
                
        
    
            
        return {"simulacion": [tabla], "colas": self.colasMaximas, "maxTCliente": self.maxTCliente}



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
        # nombre y numero servidor anterior significa "nombre y numero del servidor que finaliza su servicio"
        nombreServidorAnterior, numeroServidorAnterior = self.desamblarNombreFin(nombreFin)
        

        

        # tratamos al cliente que consumio el servicio
        if (nombreServidorAnterior != "surtidor") or (nombreServidorAnterior == "surtidor" and self.seVaDelSistema()) :
            self.clientes.eliminarCliente(nombreServidorAnterior, numeroServidorAnterior,  reloj) #Aca max T SIstema y en asignar a cola max cola
        elif (nombreServidorAnterior == "surtidor"): # si viene de surtidores y no es eliminado -> va a gomeria o a venta de accesorios
            nombreTipoServidor = self.aDondeVoy(0.4)
            nombreServidorLibre , numeroServidorLibre = self.estacion.tenesServidorDeEsteTipoLibre(nombreTipoServidor)

            # si no hay un servidor libre, asigna un cliente a cola del servidor libre
            if nombreServidorLibre == False and numeroServidorLibre == False:
                self.estacion.asignarACola(nombreTipoServidor)
                self.clientes.asignarClienteEnCola(nombreServidorAnterior, numeroServidorAnterior, nombreTipoServidor)
            # si hay un servidor libre asigna el cliente siendo atendido en el servidor libre
            elif isinstance(nombreServidorLibre, str) and isinstance(numeroServidorLibre, int):
                self.estacion.asignarServidor(nombreServidorLibre, numeroServidorLibre, reloj)# asignar servidor incluye cambiarle el estado y generar cuando va a finalizar 
                self.clientes.asignarClienteAtendido(nombreServidorAnterior, numeroServidorAnterior, nombreServidorLibre, numeroServidorLibre) 
            else:
                print("Error de logica en procesar llegada")

        # sobre el servicio que finalizo, si hay cola , hacemos atender al cliente que estaba esperando y sino ponemos al servidor libre
        if self.estacion.preguntarSiHayColaParaElTipoDeServicio(nombreServidorAnterior):
            self.estacion.asignarServidor(nombreServidorAnterior, numeroServidorAnterior, reloj)
            self.estacion.sacarDeCola(nombreServidorAnterior)
            self.clientes.atenderClienteDeCola(nombreServidorAnterior, 0)
        else:

            self.estacion.liberarServidor(nombreServidorAnterior, numeroServidorAnterior)
        
            
            
        



    def procesarLlegada(self, reloj):
        # Primero genera la proxima llegada
        self.clientes.generarProxLlegada(reloj)
        # Decide que servicio, la llegada que estamos procesando va a tomar
        nombreTipoServidor = self.decidirServidor(0.8,0.12) #Aca se pueden cambiar las probabilidades-> primer argumento carga combustible, segundo gomeria y lo q sobra ventaAccesorios
        # Pregunta si de ese tipo de servidor hay alguno libre
        nombreServidor, numeroServidor = self.estacion.tenesServidorDeEsteTipoLibre(nombreTipoServidor) # retorna False, False si no encuentra el servidor


        esteClienteVaAserVisible = False
        if self.lineaInicioSimulacion <= self.numeroIteracion <= self.lineaFinSimulacion:
                esteClienteVaAserVisible = True

        # si no hay un servidor libre, crea un cliente en cola
        if nombreServidor == False and numeroServidor == False: # Entonces no hay servidor libre
            self.estacion.asignarACola(nombreTipoServidor)
            self.clientes.crearClienteEnCola(nombreTipoServidor,reloj, esteClienteVaAserVisible)
        # si hay un servidor libre crea un cliente siendo atendido
        elif isinstance(nombreServidor, str) and isinstance(numeroServidor, int): # Hay Servidor libre!
            self.estacion.asignarServidor(nombreServidor, numeroServidor, reloj)# asignar servidor incluye cambiarle el estado y generar cuando va a finalizar 
            self.clientes.crearClienteAtendido(nombreServidor, numeroServidor, reloj, esteClienteVaAserVisible) #recordar usar el booleano que maneja que los clientes que comienzan por combustible despues pueden ir a gomeria o a compra Accesorios tambien qie se necesita la hora de llegada para despues calcular tiempo de permanencia maximo en el sistema
        else:
            print("Error de logica en procesar llegada")

        

    
    def decidirServidor(self, cargarCombustible, gomeria):
        rnd = random.random()
        gomeria = cargarCombustible + gomeria
        if rnd <= cargarCombustible:
            return "surtidor"
        elif rnd <= gomeria:
            return "gomeria"
        else:
            return "ventaAccesorios"
        
    def desamblarNombreFin(self,nombreFin):
        partes = nombreFin.split("_")
        nombreTipoServidor = partes[1]
        numeroServidor = partes[2]
        # print("El nombre tipo servidor es: " + nombreTipoServidor)
        # print("El numero de servidor es "+ numeroServidor)
        return nombreTipoServidor, numeroServidor
    
    def seVaDelSistema(self):
        if random.random() <= 0.5:
            return True
        return False
    
    def aDondeVoy(self, gomeria):
        rnd = random.random()
        if rnd <= gomeria:
            return "gomeria"
        return "ventaAccesorios"

    
    

    


            
    
    
        




