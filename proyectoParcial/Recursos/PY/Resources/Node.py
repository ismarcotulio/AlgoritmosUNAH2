# -*- coding: utf-8 -*-

from Resources.LinkedList import *

class Node:
    def __init__(self,name):
        self.name = name
        self.children = LinkedList()
        self.next = None