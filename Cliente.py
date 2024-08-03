
class Cliente:
    def __init__(self, id, estado, horaLlegada, visible):
        self.id = id
        self.estado = estado
        self.nombre = "cliente" + str(id)
        self.horaLlegada = horaLlegada
        self.visible = visible
        self.enSistema = True

    def esVisible(self):
        return self.visible
    
    def getEstado(self):
        return self.estado
    
    def getNombre(self):
        return self.nombre
