# -*- coding: utf-8 -*-

from Resources.Node import *

class Compare:
    def __init__(self):
        self.alphabeth = "°!#$%&/()=¡ 0123456789abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ"

    def greaterLength(self,str1,str2):
        l=0
        if (l<len(str1)):
            l = len(str1)
        elif (l<len(str2)):
            l = len(str2)

        return l

    def lesserLength(self,str1,str2):
        l = len(str1)
        if (l == len(str2)):
            l = len(str2)

        return l

    def compare(self,obj1,obj2):
        if (type(obj1) is Node):
            obj1 = obj1.name
        if (type(obj1) is int):
            obj1 = str(obj1)
        if (type(obj2) is Node):
            obj2 = obj2.name
        if (type(obj2) is int):
            obj2 = str(obj2)

        obj1 = obj1.strip()
        obj2 = obj2.strip()

        if (obj1 == obj2):
            return 0

        lesser = self.lesserLength(obj1,obj2)

        for i in range (lesser):

            if (self.alphabeth.index(obj1[i]) < self.alphabeth.index(obj2[i])):
                return -1
            elif (self.alphabeth.index(obj1[i]) > self.alphabeth.index(obj2[i])):
                return 1
        
        if (len(obj1) < len(obj2)):
            return -1

        return 1