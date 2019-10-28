import networkx as nx
import matplotlib.pyplot as plt

# Elements definition
class ELEMENT:
    PARLIMENT = "sejm"
    MARSHALL = "marszałek"

# Relations definition
class RELATION:
    CHOOSES = "wybiera"

# Graph initialization
G=nx.DiGraph()

# Relation definitions
G.add_edge(ELEMENT.PARLIMENT, ELEMENT.MARSHALL, relation=RELATION.CHOOSES)


# Drawing the graph
edge_labels = nx.get_edge_attributes(G,'relation')
pos = nx.planar_layout(G)
nx.draw_networkx_edge_labels(G, pos, edge_labels)
nx.draw(G, with_labels = True)
plt.show()