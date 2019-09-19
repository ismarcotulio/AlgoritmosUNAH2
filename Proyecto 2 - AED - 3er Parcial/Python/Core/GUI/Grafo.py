# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
graph = {
    "A":["B","C"],
    "B":["D","E"],
    "C":["E","F"],
    "D":["B","G"],
    "E":["B","C"],
    "F":["C","G"],
    "G":["D","F"]
}
x=10
for vertex, edges in graph.items():
    G.add_node("%s" % vertex)
    x+=2
    for edge in edges:
        G.add_node("%s" % edge)
        G.add_edge("%s" % vertex, "%s" % edge, weight = x)
        print("'%s' it connect with '%s'" % (vertex,edge))
nx.draw(G,with_labels=True)

plt.show()