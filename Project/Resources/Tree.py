from Resources.File_Node import *
from Resources.Directory_Node import *

class Tree:
    def __init__(self):
        self.root = Directory_Node("/") #Creamos el Directorio Raíz por Defecto
        
    def addChild(self,value, parent = None):
        # Debemos verificar que el archivo no exista primero
        # Una Carpeta y un Archivo pueden tener el mismo Nombre, pero 2 Carpetas ó 2 Archivos No
        
        if (parent is None):
            parent = self.root
        elif (isinstance(parent,File_Node)):
            print("Un Archivo no puede Tener hijos")
            return False

        verify = parent.children.search(value.name)
        clone = parent.children.NoDuplicate(value.name)
        
        if (verify == False and isinstance(value,File_Node)): # Si no Existe y el Nodo es de Tipo Archivo
            parent.children.add(value,parent)
            print("Mi padre es %s" %parent.children.getParent(value.name))
            print("Se Agregó el Archivo con Éxito")
            return True
        elif (verify == False and isinstance(value,Directory_Node)): # Si no Existe y el Nodo es de Tipo Carpeta
            parent.children.add(value,parent)
            print("Mi padre es %s" %parent.children.getParent(value.name))
            print("Se Agregó la Carpeta con Éxito")
            return True
        elif (verify.name == value.name and isinstance(verify,Directory_Node) and isinstance(value,File_Node) and clone == 0): #Si encuentra un nodo con el mismo nombre pero es de otro tipo entonces, lo agrega
            parent.children.add(value,parent)
            print("Mi padre es %s" %parent.children.getParent(value.name))
            print("Se Agregó el Archivo con Éxito")
            return True
        elif (verify.name == value.name and isinstance(verify,File_Node) and isinstance(value,Directory_Node) and clone == 0): #Si encuentra un nodo con el mismo nombre pero es de otro tipo, entonces lo agrega
            parent.children.add(value,parent)
            print("Mi padre es %s" %parent.children.getParent(value.name))
            print("Se Agregó la Carpeta con Éxito")
            return True
        else:
            if (isinstance(value,File_Node)):
                print("El archivo %s ya existe en éste Directorio" %value.name)
                return False
            else:
                print("La Carpeta %s ya existe en éste Directorio" %value.name)
                return False

    def protection(self,name,parent = None):
        if (parent is None):
            parent = self.root

        return parent.children.NoDuplicate(name)