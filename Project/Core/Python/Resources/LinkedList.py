#Linked List almacena onjetos tipo Connect_Nodes los cuales se encargan de toda la estructura del Árbol

from Core.Python.Resources.Compare import *
from Core.Python.Resources.Directory_Node import *
from Core.Python.Resources.File_Node import *

class LinkedList:
    def __init__(self):
        self.first = None
        self.count = 0
        self.compare = Compare()
         #Se encarga de contar cuantos elementos hay en la lista enlazada

    def add(self,item, parent): #Función para agregar cualquier Nodo
        self.AddInner(self.first,item,parent)
        self.count+=1

    def AddInner(self, current,item,parent):
        if self.first is None:
            print("creacion raiz")
            self.first = item
            self.first.parent = parent
            return True
        else:
            if isinstance(item,Directory_Node) == True:
                current = self.first
                if isinstance(current,Directory_Node)==True:
                    if self.compare.compare(item,current) < 0:
                        print("item menor que la raiz")
                        self.first = item
                        self.first.next = current
                        self.first.parent = parent
                        return True
                        
                    elif self.compare.compare(item,current) == 0:
                        print("item igual que la raiz")
                        self.first = item
                        self.first.next = current.next
                        self.first.parent = parent
                        return True
                    
                    else:
                        print("item mayor que la raiz")
                        while current.next and isinstance(current.next,Directory_Node)==True:
                            previous = current
                            current = current.next
                            if self.compare.compare(item,current) < 0:
                                previous.next = item
                                previous.next.next = current
                                previous.next.parent = parent
                                return True                    
                            elif self.compare.compare(item,current) == 0:
                                previous.next = item
                                previous.next.next = current.next
                                previous.next.parent = parent
                                return True                
                        if isinstance(current.next,File_Node) == True:
                            previous = current
                            current = current.next
                            previous.next = item
                            previous.next.next = current
                            previous.next.parent = parent
                            return True


                        if current.next is None:
                            current.next = item
                            current.next.parent = parent 
                        return True
                elif isinstance(current,File_Node)==True:
                    self.first = item
                    self.first.next = current
                    self.first.parent = parent
                    return True

            elif isinstance(item,File_Node)==True:
                current = self.first
                if isinstance(current,File_Node)==True:

                    if self.compare.compare(item,current) < 0:
                        print("item menor que la raiz")
                        self.first = item
                        self.first.next = current
                        self.first.parent = parent
                        return True
                        
                    elif self.compare.compare(item,current) == 0:
                        print("item igual que la raiz")
                        self.first = item
                        self.first.next = current.next
                        self.first.parent = parent
                        return True
                    
                    else:
                        print("item mayor que la raiz")
                        while current.next:
                            previous = current
                            current = current.next
                            if self.compare.compare(item,current) < 0:
                                previous.next = item
                                previous.next.next = current
                                previous.next.parent = parent
                                return True                    
                            elif self.compare.compare(item,current) == 0:
                                previous.next = item
                                previous.next.next = current.next
                                previous.next.parent = parent
                                return True                
                        
                        current.next = item
                        current.next.parent = parent 
                        return True
                elif isinstance(current,Directory_Node) == True:
                    current = self.first
                    while isinstance(current.next,Directory_Node):
                        current = current.next
                    if current.next != None:
                        previous = current
                        current = current.next
                        if self.compare.compare(item,current) < 0:
                            print("item menor que la raiz")
                            previous.next = item
                            previous.next.next = current
                            previous.next.parent = parent
                            return True
                            
                        elif self.compare.compare(item,current) == 0:
                            print("item igual que la raiz")
                            previous.next = item
                            previous.next.next = current.next
                            previous.next.parent = parent
                            return True
                        
                        else:
                            print("item mayor que la raiz")
                            while current.next:
                                previous = current
                                current = current.next
                                if self.compare.compare(item,current) < 0:
                                    previous.next = item
                                    previous.next.next = current
                                    previous.next.parent = parent
                                    return True                    
                                elif self.compare.compare(item,current) == 0:
                                    previous.next = item
                                    previous.next.next = current.next
                                    previous.next.parent = parent
                                    return True                
                            
                            current.next = item
                            current.next.parent = parent 
                            return True
                    else:
                        current = self.first
                        while current.next:
                            current = current.next
                        current.next = item
                        current.next.parent = parent

    def search(self,name): #Función de búsqueda, devuelve la primera Instancia encontrada
        return self.SearchInner(self.first,name)

    def SearchInner(self,current,name):
        if (current is None):
            return False
        elif (current.name == name):
            return current
        else:
            return self.SearchInner(current.next, name) 

    def _delete(self, name):
        if (self.first is None):
            print("No hay nada que borrar")
            return False
        elif (self.first.next is None and self.first.name == name):
            self.SubTree(self.first)
            self.first = None
            print ("Se borró el nodo %s con exito" % name)
            self.count -=1
            return True
        elif (self.first.next and self.first.name == name):
            self.SubTree(self.first)
            current = self.first
            self.first = self.first.next
            current.next = None
            print ("Se borró el nodo %s con exito" % name)
            self.count -=1
            return True
        else:
            current = self.first 
            previous = current
            while (current.next and current.name != name):
                previous = current
                current = current.next
            self.SubTree(current)
            previous.next = current.next 
            current.next = None
        self.count -= 1
        print ("Se borró el nodo %s con exito" % name)
        return True

    def getParent(self,value): # Devuelve quien es el padre de cualquier nodo
        return self.getInnerParent(self.first,value)

    def getInnerParent(self,current,name):
        if (current is None):
            return False
        elif (current.name == name):
            return current.parent.name
        else:
            return self.getInnerParent(current.next, name) 

    def getChild(self,value): # Devuelve quien es el padre de cualquier nodo
        return self.getInnerChild(self.first,value)

    def getInnerChild(self,current,name):
        if (current is None):
            return False
        elif (current.name == name):
            return current
        else:
            return self.getInnerChild(current.next, name) 

    def NoDuplicate(self,name): #Ésta Funcion sirve para proteger la lista de archivos o Carpetas repetidas
        current = self.first
        verify = 0
        if (current is None):
            return verify
        else:
            while(current.next):
                if (current.name == name):
                    verify += 1
                current = current.next
        return verify

    def SubTree(self, node):
        queue = []

        if (isinstance(node,File_Node)):
            queue.append(node)
        elif (isinstance(node,Directory_Node)):
            if (node.children != None):
                current = node.children.first
                while (current != None):
                    queue.append(current)
                    current = current.next
                for i in range (len(queue)):
                    self.SubTree(queue[i])
        for i in range(len(queue)):
            print("Se borró el Nodo %s" % queue[i].name)
            queue[i] = None
