# Directory Node es una clase que almacenará Listas Enlazadas como hijos
# y dentro de ellas podra Almacenar Nodos Tipo File o nuevas Listas enlazadas

from Resources.LinkedList import *

class Directory_Node:
    def __init__(self,name):
        self.name = name
        self.children = LinkedList() #Ya que es una carpeta esta tendrá una Lista Enlazada para almacenar hijos
