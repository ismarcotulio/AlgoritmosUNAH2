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

        #nx.shortest_path_length(G, source=node_1, target=node_2, weight='weight')

        #nx.dijkstra_path(G,source=)

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
        return w.getWeight(float(p[0]),float(p[1]),int(p[2]),float(p[3]),p[4])
