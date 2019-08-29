class LinkedList:
    def __init__(self):
        self.first = None
        self.count = 0

    def add(self, value,parent):
        self.AddInner(self.first, value, parent)
        self.count += 1

    def AddInner(self, current, value, parent):
        if (current is None):
            self.first = value
            value.parent = parent
        elif (current.next is None):
            current.next = value
            value.parent = parent
        else:
            self.AddInner(current.next,value,parent)

    def search(self,name): #Este Método busca en la lista actual no en todo el árbol
        return self.searchInner(self.first, name)

    def searchInner(self,current, name):
        if (current is None):
            return False
        elif (current.name == name):
            return current
        else:
            return self.searchInner(current.next,name)

    def getParent(self,name): #Devuelve el padre de cualquier nodo en la lista actual
        return self.getInnerParent(self.first, name)

    def getInnerParent(self, current, name):
        if (current is None):
            return False
        elif (current.name == name):
            return current.parent
        else:
            return self.getInnerParent(current.next, name)

    def NoDuplicate(self,name): #Sirve para proteger a la lista de archivos o carpetas repetidas
        current = self.first
        verify = 0
        if (current is None):
            return verify
        else:
            while(current.next):
                if (current.name == name):
                    verify +=1
                current = current.next
        return verify

    def getChildrenList(self):
        children = [".",".."]
        current = self.first 
        if (current is None):
            return children
        elif (current.parent == "/"):
            children = []
            while (current.next != None):
                children.append(current)
                current = current.next
            children.append(current)
        else:
            while (current.next != None):
                children.append(current)
                current = current.next
            children.append(current)
        return children

    def delete(self):
        pass