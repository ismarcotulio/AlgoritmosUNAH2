class AlgoritFloyd:

    def _init_(self):
        pass

    def minimo(self,num1,num2):
        minimo = num1
        if(minimo >num2):
            minimo = num2
        
        return minimo
                
    def caminosR(self,i,k,caminosAuxiliares,caminoRecorrido):
        if caminosAuxiliares[i][k] == "" :
            return ""
        else:
            #recursividad
            caminoR = caminoR +"%s %s," %(self.caminosRecorrido(i,caminosAuxiliares[i][k],caminosAuxiliares,caminoRecorrido),(int(caminosAuxiliares[i][k])+1))
        return caminoR

    def AlgoritFloyd(self,matriz):

        vertices = len(matriz)
        alfabeth = ["A","B","C","D","E","F","G","H","I","J","K","L","N","M"]
        matrizAdyacencia = matriz
        caminos =[[""]*vertices for i in range(vertices)]
        caminosAuxiliares = [[""]*vertices for i in range(vertices)]
        caminoRecorrido=""
        cadena=""
        caminitos=""
        w = ""
       
        for k in range(vertices):
            for i in range(vertices):
                for j in range(vertices):
                    temporal1 = matrizAdyacencia[i][j]
                    temporal2 = matrizAdyacencia[i][k]
                    temporal3 = matrizAdyacencia[k][j]
                    temporal4 = temporal2 + temporal3

                    minimo = self.minimo(temporal1,temporal4)
                    
                    if temporal1 != temporal4:
                        if(minimo == temporal4):
                            caminoRecorrido = ""
                            
                            caminosAuxiliares[i][j] = "%s " %(k)
                            w = "%s %s"%((self.caminosR(i,k,caminosAuxiliares,caminoRecorrido),(k+1)))
                            caminos[i][j] =w
                        matrizAdyacencia[i][j]= minimo
    
        for i in range(vertices):
            for j in range(vertices):
                cadena = "%s [%s]" %(cadena,matrizAdyacencia[i][j])
            cadena = "%s \n" %(cadena)
        
        #--------------------
        for i in range(0,vertices):
            for j in range(0,vertices):
                if matrizAdyacencia[i][j] !=999999999:
                    if i != j:
                        if caminos[i][j] == "":
                            caminitos = caminitos + "De (%s---->%s) Irse por....(%s , %s)\n" %((alfabeth[i]),(alfabeth[j]),(alfabeth[i]),(alfabeth[j]))
                        else:
                        #    t = len(caminos)
                            caminitos = caminitos + "De (%s---->%s) Irse por....(%s , %s, %s)\n" %((alfabeth[i]),(alfabeth[j]),(alfabeth[i]),alfabeth[int(caminos[i][j])-1],(alfabeth[j]))
        
        return "Los caminos mas cortos entre Vertices son: \n%s" %(caminitos)
    
    #-------------------------------------------------------------------------------------------------------------------------------------
    #devolviendo en tipo matriz el analisis de los caminos mas cortos.
    def AlgoritFloyd2(self,matriz):

        vertices = len(matriz)
        alfabeth = ["A","B","C","D","E","F","G","H","I","J","K","L","N","M"]
        matrizAdyacencia = matriz
        caminos =[[""]*vertices for i in range(vertices)]
        caminosAuxiliares = [[""]*vertices for i in range(vertices)]
        caminoRecorrido=""
        caminitos=""
        w = ""
    
        for k in range(vertices):
            for i in range(vertices):
                for j in range(vertices):
                    temporal1 = matrizAdyacencia[i][j]
                    temporal2 = matrizAdyacencia[i][k]
                    temporal3 = matrizAdyacencia[k][j]
                    temporal4 = temporal2 + temporal3

                    minimo = self.minimo(temporal1,temporal4)
                    
                    if temporal1 != temporal4:
                        if(minimo == temporal4):
                            caminoRecorrido = ""
                            caminosAuxiliares[i][j] = "%s " %(k)
                            w = w + self.caminosR(i,k,caminosAuxiliares,caminoRecorrido)
                            w= w+str(k+1)
                            caminos[i][j] =w
                        matrizAdyacencia[i][j]= minimo
        return matrizAdyacencia
