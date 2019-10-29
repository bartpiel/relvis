import networkx as nx
import matplotlib.pyplot as plt

# Elements definition
class ELEMENT:
    PARLIMENT = "sejm"
    MARSHALL = "marszałek"
    VICEMARSHALL = "wicemarszałek"
    MARSHALL_SENIOR = "marszałek senior"
    PRESIDENT = "president"
    SECRETARY = "sekretarz"
    TEMPORARY_SECRETARY = "sekretarz tymczasowy"
    PRESIDIUM = "prezydium"
    PRIME_MINISTER = "prezes rady ministrów"
    COUNCIL_OF_MINISTERS = "rada ministrów"
    COMMITTEE = "komisja"
    REPRESENTATIVE = "poseł"
    CLUB = "klub poselski"
    CIRCLE = "koło poselski"

# Relations definition
class RELATION:
    INTITUTES = "powołuje"
    CHOOSES = "wybiera"
    CONDUCTS_CHOICE = "przeprowadza wybór"
    COMMANDS_CHOICE = "zarządza wybór"
    SUGGESTS_CANDIDATE = "zgłasza kandydata"
    DEMITS = "składa dymisję"
    IS_MEMBER = "jest członkiem"
    OBEYS_COMMANDS = "stosuje się do poleceń"
    GRANTS_VACATION = "udziela urlopu"

# Graph initialization
G=nx.DiGraph()

# Relation definitions
# Art. 1 p. 1
G.add_edge(ELEMENT.PRESIDENT, ELEMENT.MARSHALL_SENIOR, relation=RELATION.INTITUTES)
# Art. 2 p. 2
G.add_edge(ELEMENT.MARSHALL_SENIOR, ELEMENT.TEMPORARY_SECRETARY, relation=RELATION.CHOOSES)
# Art. 4 p. 3
G.add_edge(ELEMENT.PARLIMENT, ELEMENT.MARSHALL, relation=RELATION.CHOOSES)
# Art. 5 p. 5
G.add_edge(ELEMENT.MARSHALL, ELEMENT.VICEMARSHALL, relation=RELATION.COMMANDS_CHOICE)
# Art. 6 p. 1
G.add_edge(ELEMENT.PARLIMENT, ELEMENT.SECRETARY, relation=RELATION.CHOOSES)
# Art. 6 p. 2
G.add_edge(ELEMENT.PRESIDIUM, ELEMENT.SECRETARY, relation=RELATION.SUGGESTS_CANDIDATE)
# Art. 6a
G.add_edge(ELEMENT.PRIME_MINISTER, ELEMENT.COUNCIL_OF_MINISTERS, relation=RELATION.DEMITS)
# Art. 7 p. 1
G.add_edge(ELEMENT.REPRESENTATIVE, ELEMENT.COMMITTEE, relation=RELATION.IS_MEMBER, may = TRUE)
# Art. 7 p. 3
G.add_edge(ELEMENT.REPRESENTATIVE, ELEMENT.COUNCIL_OF_MINISTERS, relation=RELATION.IS_MEMBER, may = TRUE)
# Art. 7 p. 2 pdp. 2
G.add_edge(ELEMENT.REPRESENTATIVE, ELEMENT.COMMITTEE, relation=RELATION.OBEYS_COMMANDS)
# Art. 7 p. 8 pdp. 4
G.add_edge(ELEMENT.MARSHALL, ELEMENT.REPRESENTATIVE, relation=RELATION.GRANTS_VACATION, may=TRUE)
# Art. 8 p. 1
G.add_edge(ELEMENT.REPRESENTATIVE, ELEMENT.CLUB, relation=RELATION.IS_MEMBER, may = TRUE)
# Art. 8 p. 1
G.add_edge(ELEMENT.REPRESENTATIVE, ELEMENT.CIRCLE, relation=RELATION.IS_MEMBER, may = TRUE)

# Drawing the graph
edge_labels = nx.get_edge_attributes(G,'relation')
pos = nx.planar_layout(G)
nx.draw_networkx_edge_labels(G, pos, edge_labels)
nx.draw(G, with_labels = True)
plt.show()