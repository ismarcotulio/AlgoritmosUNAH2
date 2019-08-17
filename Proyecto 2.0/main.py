# -*- cofing: utf-8 -*-

from Resources.File_Node import *
from Resources.Directory_Node import *
from Resources.Connect_Nodes import *
from Resources.LinkedList import *
from Resources.Tree import *

bonsai = Tree() #Creamos un Nuevo Árbol
n1 = File_Node("Threshold") #Nuevo Nodo de tipo Archivo
n2 = Directory_Node("home/") #Nuevo Nodo de Tipo Carpeta
bonsai.addChild(n1) #Agregamos al árbol el nodo n1
bonsai.addChild(n2) #Agregamos al árbol el nodo n2
bonsai.addChild(n1) #Intentamos agregar el Nodo n1 nuevamente
bonsai.addChild(n2) #Intentamos agregar el Nodo n2 nuevamente

n3 = File_Node("Alexis") #Nuevo Nodo tipo archivo
bonsai.addChild(n3,n2) #añadimos el nodo n3 en la carpeta n2 (home/)
bonsai.addChild(n3) #agregamos el nodo n3 en la raíz