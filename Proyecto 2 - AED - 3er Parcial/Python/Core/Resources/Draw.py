import networkx as nx
import matplotlib.pyplot as plt
from Core.Resources.weight import *

class Draw_Graph:

    def __init__(self):
        pass

    def draw(self,graph):
        
        G = self.Draw_Inner(graph)

        # Crear todas las posiciones de los vertices y guardarlas
        pos = nx.spring_layout(G)

        # Dibujar el Grafo de acuerdo a las posiciones generadas
        nx.draw(G, pos, with_labels=True, node_color= 'b', edge_color = 'g', arrowsize=10)

        # Crear las etiquetas para los pesos
        labels = nx.get_edge_attributes(G,'weight')

        # Dibujar las etiquetas de peso de acuerdo a la posicion de los vertices
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        plt.show()

    def Draw_Inner(self,graph):
        G = nx.Graph()
        for k,v in graph.items():
            G.add_node("%s" % k)
            for d in v:
                self.add_Vertices(d,G,k)
        return G

    def add_Vertices(self,graph,G,vertex):
        for k,v in graph.items():
            G.add_node("%s" % k)
            print("'%s' it connects with '%s'" % (vertex,k))
            G.add_edge("%s" % vertex, "%s" % k, weight = self.calculate_Weight(v))
        return G

    def calculate_Weight(self,properties):
        p = list(properties.values())
        w = Weight()
        return w.getWeight(int(p[0]),int(p[1]),int(p[2]),int(p[3]),p[4])
