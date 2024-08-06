from Eventos import *
from Cliente import *

class Clientes:
    def __init__(self, media, desviacion):
        self.vClientes = [] 
        self.proximaLlegada = Llegada(media,  desviacion)
        self.proximoId = 1
        self.maxTCliente = 0

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
        continuacionNombre =  str(self.proximoId)
        nombreLlegada += continuacionNombre
        return tLlegada, nombreLlegada

    def generarProxLlegada(self, reloj):
        self.proximaLlegada.generarProximaLlegada(reloj)

    def crearClienteAtendido(self,  tipoServidor, numeroServidor , horaLlegada, seraVisible): 
        id = self.proximoId
        self.proximoId += 1
        estado = "C_"+ str(id) + "_"+ "SA_" + str(tipoServidor) + "_" + str(numeroServidor)
        cliente = Cliente(id, estado, horaLlegada, seraVisible)
        self.vClientes.append(cliente)

    def crearClienteEnCola(self, tipoServidor, horaLlegada, seraVisible):
        id = self.proximoId
        self.proximoId += 1
        estado = "C_"+ str(id) + "_" + "enCola_" + str(tipoServidor) + "_" + "0"
        cliente = Cliente(id, estado, horaLlegada, seraVisible)
        self.vClientes.append(cliente)

    def asignarClienteAtendido(self, tipoServidorAnterior, numeroServidorAnterior, tipoServidorNuevo, numeroServidorNuevo):
        id = self.buscarCliente(tipoServidorAnterior, numeroServidorAnterior)
        for cliente in self.vClientes:
            if cliente.getId() == id:
                cliente.serAtendido(tipoServidorNuevo, numeroServidorNuevo)

    def asignarClienteEnCola(self, tipoServidorAnterior, numeroServidorAnterior, tipoServidorNuevo):
        id = self.buscarCliente(tipoServidorAnterior, numeroServidorAnterior)
        for cliente in self.vClientes:
            if cliente.getId() == id:
                cliente.aCola(tipoServidorNuevo)

    def atenderClienteDeCola(self, tipoServidorQueLeAsignare, numeroServidorQueLeAsignare):
        id = self.buscarCliente(tipoServidorQueLeAsignare, numeroServidorQueLeAsignare )
        for cliente in self.vClientes:
            if cliente.getId() == id:
                cliente.serAtendido(tipoServidorQueLeAsignare, numeroServidorQueLeAsignare)

    def eliminarCliente(self, tipoServidorAnterior, numeroServidorAnterior,  reloj):
        id = self.buscarCliente(tipoServidorAnterior, numeroServidorAnterior)
        for i in range(len(self.vClientes)):
            if self.vClientes[i].getId() == id:
                # Esto para calcular el tiempo del cliente en el sistema
                tCliente = reloj - self.vClientes[i].getHoraLlegada()
                if tCliente > self.maxTCliente:
                    self.maxTCliente = tCliente
                # y aca se elimina
                self.vClientes.remove(self.vClientes[i])
                break
                

    
    def buscarCliente(self, tipoServidorAnterior, numeroServidorAnterior): #les pase el servidor q estaba libre. necesito pasarles ademas el servidor anterior
        for cliente in self.vClientes:
            estadoCliente = cliente.getEstado()
            vEstado = estadoCliente.split('_')
            id = vEstado[1]
            tipoServidorTransitorio = vEstado[3]
            numeroServidorTransitorio = vEstado[4]
            if tipoServidorTransitorio == tipoServidorAnterior and numeroServidorTransitorio == str(numeroServidorAnterior):
                return int(id)
            
    def getMaxTCliente(self):
        return self.maxTCliente

            
