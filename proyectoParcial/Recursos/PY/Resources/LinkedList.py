# -*- coding: utf-8 -*-

from Resources.Node import *
from Resources.Compare import *

class LinkedList:
    def __init__(self):
        self.first = None

    def addLinkedList(self,value):
        if (not self.first):
            self.first = Node(value)
        else:
            compare = Compare()
            if(compare.compare(self.first,value)>0):
                stack = self.first
                self.first = Node(value)
                self.first.next = stack
                return True
            else:
                previous = self.first
                current = self.first.next

                while(current):
                    if (compare.compare(current,value)<0):
                        previous = current
                        current = current.next
                        return True
                    elif (compare.compare(current,value)>0):
                        stack = current
                        previous.next = Node(value)
                        previous.next.next = stack
                        return True
                    else:
                        previous.next = Node(value)
                        previous.next.next = current.next
                        return True

                previous.next = Node(value)
                return True