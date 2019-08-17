#Esta Clase es la que se encarga de enlazar y conectar los Nodos con su Hermanos y Padres

class Connect_Nodes:
    def __init__(self,value,parent = None, next = None):
        self.parent = parent
        self.value = value
        self.next = next

