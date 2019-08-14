# -*- coding: utf-8 -*-

from Resources.LinkedList import *
from Resources.Node import *

class Tree:
    def __init__(self):
        self.root = LinkedList()

    def addTree(self, value, parent = None):
        if (parent == None):
            parent = self.root

        parent.addLinkedList(value)