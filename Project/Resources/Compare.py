from Resources.File_Node import *
from Resources.Directory_Node import *

class Compare:
    def __init__(self):
        self.alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def lesserLength(self, str1, str2):
        lesser = len(str1)
        if len(str2) < len(str1):
            lesser = len(str2)
        return lesser


    def compare(self, str1, str2, num1=None, num2=None):
        if isinstance(str1,(int, float)) == True:
            num1 = str1
            str1 = str(str1)
        if isinstance(str2,(int, float)) == True:
            num2 = str2
            str2 = str(str2)
        if isinstance(str1, Directory_Node) == True or isinstance(str1, File_Node) == True:
            str1 = str(str1.name)
        if isinstance(str2, Directory_Node) == True or isinstance(str2, File_Node) == True:
            str2 = str(str2.name)

        if num1!=None and num2!=None:
            if num1 > num2:
                return 1
            elif num1 == num2:
                return 0
            else:
                return -1
        else:
            lesser = self.lesserLength(str1,str2)
            for i in range(lesser):
                if self.alphabet.index(str1[i]) > self.alphabet.index(str2[i]):
                    return 1
                elif self.alphabet.index(str1[i]) < self.alphabet.index(str2[i]):
                    return -1
                else:

                    if len(str1) == len(str2):
                        return 0

                    elif(len(str1) == lesser):
                        return -1

                    else:
                        return 1
       





