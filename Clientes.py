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

    def asignarClienteAtendido(self, nombreTipoServidor, numeroServidor):
        cliente = self.buscarCliente(nombreTipoServidor, numeroServidor)
        cliente.serAtendido(nombreTipoServidor, numeroServidor)

    def asignarClienteEnCola(self, nombreTipoServidor):
        cliente = self.buscarCliente(nombreTipoServidor, 0)
        cliente.aCola(nombreTipoServidor)

    
    def buscarCliente(self, tipoServidor, numeroServidor):
        for cliente in self.vClientes:
            estadoCliente = cliente.getEstado()
            vEstado = estadoCliente.split('_')
            # id = vEstado[1]
            tipoServidorTransitorio = vEstado[3]
            numeroServidorTransitorio = vEstado[5]
            if tipoServidorTransitorio == tipoServidor and numeroServidorTransitorio == numeroServidor:
                return cliente

            
