from Eventos import *
from Cliente import *

class Clientes:
    def __init__(self, media, desviacion):
        self.vClientes = [] 
        self.proximaLlegada = Llegada(media,  desviacion)

    def vectorizarLlegada(self):
        return self.proximaLlegada.vectorizar()
    
    def titularizarLlegada(self):
        return self.proximaLlegada.titularizar()
    
    def vectorizarClientes(self):
        vAux = []
        for cliente in self.vClientes:
            if cliente.esVisible():
                vAux.append(cliente.getEstado())
        return vAux
    
    
    def getProxLlegada(self):
        tLlegada = self.proximaLlegada.getProxLlegada()
        nombreLlegada = "llegadaCliente_"
        continuacionNombre = str(len(self.vClientes) + 1) 
        nombreLlegada += continuacionNombre
        return tLlegada, nombreLlegada

    def generarProxLlegada(self, reloj):
        self.proximaLlegada.generarProximaLlegada(reloj)

    def crearClienteAtendido(self,  tipoServidor, numeroServidor , horaLlegada, seraVisible): 
        #recordar usar el booleano que maneja 
        # que los clientes que comienzan 
        # por combustible despues pueden ir a gomeria o a compra Accesorios
        # tambien qie se necesita la hora de llegada para despues calcular 
        # tiempo de permanencia maximo en el sistema
        id = len(self.vClientes) + 1
        estado = "C_"+ str(id) + "_"+ "SA_" + str(tipoServidor) + "_" + str(numeroServidor)
        cliente = Cliente(id, estado, horaLlegada, seraVisible)
        self.vClientes.append(cliente)

    def crearClienteEnCola(self, tipoServidor, horaLlegada, seraVisible):
        id = len(self.vClientes) + 1
        estado = "C_"+ str(id) + "_" + "enCola_" + str(tipoServidor) + "_" + "0"
        cliente = Cliente(id, estado, horaLlegada, seraVisible)
        self.vClientes.append(cliente)

    def asignarClienteAtendido(self, tipoServidorAnterior, numeroServidorAnterior, tipoServidorNuevo, numeroServidorNuevo):
        id = self.buscarCliente(tipoServidorAnterior, numeroServidorAnterior)
        for cliente in self.vClientes:
            if cliente.getId() == id:
                cliente.serAtendido(tipoServidorNuevo, numeroServidorNuevo)

    def asignarClienteEnCola(self, tipoServidorAnterior, numeroServidorAnterior, nombreTipoServidor):
        id = self.buscarCliente(tipoServidorAnterior, numeroServidorAnterior)
        for cliente in self.vClientes:
            if cliente.getId() == id:
                cliente.aCola(nombreTipoServidor)

    
    def buscarCliente(self, tipoServidorAnterior, numeroServidorAnterior): #les pase el servidor q estaba libre. necesito pasarles ademas el servidor anterior
        for cliente in self.vClientes:
            estadoCliente = cliente.getEstado()
            vEstado = estadoCliente.split('_')
            id = vEstado[1]
            tipoServidorTransitorio = vEstado[3]
            numeroServidorTransitorio = vEstado[4]
            if tipoServidorTransitorio == tipoServidorAnterior and numeroServidorTransitorio == numeroServidorAnterior:
                return id

            
