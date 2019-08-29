#Linked List almacena onjetos tipo Connect_Nodes los cuales se encargan de toda la estructura del Árbol


class LinkedList:
    def __init__(self):
        self.first = None
        self.count = 0 #Se encarga de contar cuantos elementos hay en la lista enlazada

    def add(self,item, parent): #Función para agregar cualquier Nodo
        self.AddInner(self.first,item,parent)
        self.count+=1

    def AddInner(self, current,item,parent):
        if (current is None):
            self.first = item
            self.first.parent = parent
        elif (current.next is None):
            current.next = item
            current.next.parent = parent
        else:
            self.AddInner(current.next,item,parent)

    def search(self,name): #Función de búsqueda, devuelve la primera Instancia encontrada
        return self.SearchInner(self.first,name)

    def SearchInner(self,current,name):
        if (current is None):
            return False
        elif (current.name == name):
            return current
        else:
            return self.SearchInner(current.next, name) 

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