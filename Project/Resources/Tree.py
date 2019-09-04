from Resources.LinkedList import *

class Tree:
    def __init__(self):
        self.root = Directory_Node("/") #Creamos el Directorio Raíz por Defecto
        
    def addChild(self,item, parent = None):
        # Debemos verificar que el archivo no exista primero
        # Una Carpeta y un Archivo pueden tener el mismo Nombre, pero 2 Carpetas ó 2 Archivos No
        
        if (parent is None):
            parent = self.root
        elif (isinstance(parent,File_Node)):
            print("Un Archivo no puede Tener hijos")        
            return False
        if parent.children == None:
            parent.children = LinkedList()

        verify = parent.children.search(item.name)
        clone = parent.children.NoDuplicate(item.name)
        
        if (verify == False and isinstance(item,File_Node)): # Si no Existe y el Nodo es de Tipo Archivo
            parent.children.add(item,parent)
            print("Mi padre es %s" %parent.children.getParent(item.name))
            print("Se Agregó el Archivo con Éxito")
            return True
        elif (verify == False and isinstance(item,Directory_Node)): # Si no Existe y el Nodo es de Tipo Carpeta
            parent.children.add(item,parent)
            print("Mi padre es %s" %parent.children.getParent(item.name))
            print("Se Agregó la Carpeta con Éxito")
            return True
        elif (verify.name == item.name and isinstance(verify,Directory_Node) and isinstance(item,File_Node) and clone == 0): #Si encuentra un nodo con el mismo nombre pero es de otro tipo entonces, lo agrega
            parent.children.add(item,parent)
            print("Mi padre es %s" %parent.children.getParent(item.name))
            print("Se Agregó el Archivo con Éxito")
            return True
        elif (verify.name == item.name and isinstance(verify,File_Node) and isinstance(item,Directory_Node) and clone == 0): #Si encuentra un nodo con el mismo nombre pero es de otro tipo, entonces lo agrega
            parent.children.add(item,parent)
            print("Mi padre es %s" %parent.children.getParent(item.name))
            print("Se Agregó la Carpeta con Éxito")
            return True
        else:
            if (isinstance(item,File_Node)):
                print("El archivo %s ya existe en éste Directorio" %item.name)
                return False
            else:
                print("La Carpeta %s ya existe en éste Directorio" %item.name)
                return False

    def moveTo(self, value, parent = None):
        if (parent is None):
            parent = self.root

        self.root = parent.children.getChild(value)
        print("La ruta actual es %s"%self.root.name)
        return True

    def protection(self,name,parent = None):
        if (parent is None):
            parent = self.root

        return parent.children.NoDuplicate(name)

    def traversal(self, node):
        if isinstance(node,Directory_Node) == True:
            print("directorio"+str(node.name))
            queue = []
            current = node.children.first
            while current != None:
                queue.append(current)
                current = current.next
            for i in range(len(queue)):
                self.traversal(queue[i])
        else:
            print("Archivo:"+str(node.name))

    def getFirstRoot(self, node):
        while node.parent != None:
            node = node.parent
        return node