class MatrixAdyacente:
    def _init_ (self):
        pass


    def MatrixAdyacente(self,grafo):
        tam = len(grafo)
        m = [[999999999]*tam for i in range(tam)]
        
        
        alfabet = "ABCDEFGHIJKNMOPQRST"
        cont =0
        fila=0
        colum=1
        m[fila][colum] = 11
        
        for k,v in grafo.items():
            colum =0
            for t,j in v[0].items():
                if fila != colum:
                    if alfabet.index(t) == colum:
                        
                        c = v[0][t]["distancia"]
                        m[fila][colum]=c
                        colum=colum+1
                    else:
                        di = alfabet.index(t)-colum
                        colum = colum+di
                        c = v[0][t]["distancia"]
                        m[fila][colum]=c
                        colum=colum+1

                else:
                    if alfabet.index(t) != colum:
                        di = alfabet.index(t)-colum;
                        colum = colum+di
                        c = v[0][t]["distancia"]
                        m[fila][colum]=c
                        colum = colum+1
                    else:
                        m[fila][colum] = 0
                        colum = colum+1

            fila = fila +1

        return m
