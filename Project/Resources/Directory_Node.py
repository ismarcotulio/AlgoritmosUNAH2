from Resources.LinkedList import *

class Directory_Node:
    def __init__(self,name):
        self.name = name
        self.children = LinkedList()
        self.next = None
        self.parent = None

    def getChildren(self):
        return self.children.getChildrenList()
