import networkx as nx
import matplotlib.pyplot as plt

# Elements definition
class ELEMENT:
    PARLIMENT = "sejm"
    MARSHALL = "marszałek"
    VICE_MARSHALL = "wicemarszałek"
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
    CHIEF_OF_REGISTARS_OFFICE = "szef kancelarii sejmu"
    VICE_CHIEF_OF_REGISTARS_OFFICE = "zastępca szefa kancelarii sejmu"
    SENIOR_CONVENT = "konwent seniorów"
    CHIEF_OF_CLUB = "przewodniczący klubu"
    VICE_CHIEF_OF_CLUB = "wiceprzewodniczący klubu"
    SPECIAL_COMMITTEE = "komisja nadzwyczajna"
    FORENSIC_COMMITTEE = "komisja śledcza"
    CHIEF_OF_COMMITTEE = "szef komisji"
    PRESIDIUM_OF_COMMITTEE = "prezydium komisji"
    CHIEF_OF_COMMITTEE = "przedowniczący komisji"
    VICE_CHIEF_OF_COMMITTEE = "wiceprzedowniczący komisji"
    
# Relations definition
class RELATION:
    INSTITUTES = "powołuje"
    CHOOSES = "wybiera"
    CONDUCTS_CHOICE = "przeprowadza wybór"
    COMMANDS_CHOICE = "zarządza wybór"
    SUGGESTS_CANDIDATE = "zgłasza kandydata"
    DEMITS = "składa dymisję"
    IS_MEMBER = "jest członkiem"
    OBEYS_COMMANDS = "stosuje się do poleceń"
    GRANTS_VACATION = "udziela urlopu"
    REPRESENTS = "reprezentuje"
    LEADS = "przewodzi"
    HELPS = "udziela pomocy"
    CANCELS = "odwołuje"
    CONSULTS_WITH = "konsultuje się z"
    SUBSTITUTES = "zastępuje"
    DECIDES_BUDGET = "decyduje o budżecie"
    WARN = "zwrócić uwagę/upomnieć/udzielić nagany"
    DECREASE_DIET = "zmniejszyć dietę"
    EXCLUDE_FROM_PRECEEDINGS = "wyklucza z obrad"


# Graph initialization
G=nx.DiGraph()

# Relation definitions
# Art. 1 p. 1
G.add_edge(ELEMENT.PRESIDENT, ELEMENT.MARSHALL_SENIOR, relation=RELATION.INSTITUTES)
# Art. 2 p. 2
G.add_edge(ELEMENT.MARSHALL_SENIOR, ELEMENT.TEMPORARY_SECRETARY, relation=RELATION.CHOOSES)
# Art. 4 p. 3
G.add_edge(ELEMENT.PARLIMENT, ELEMENT.MARSHALL, relation=RELATION.CHOOSES)
# Art. 5 p. 5
G.add_edge(ELEMENT.MARSHALL, ELEMENT.VICE_MARSHALL, relation=RELATION.COMMANDS_CHOICE)
# Art. 6 p. 1
G.add_edge(ELEMENT.PARLIMENT, ELEMENT.SECRETARY, relation=RELATION.CHOOSES)
# Art. 6 p. 2
G.add_edge(ELEMENT.PRESIDIUM, ELEMENT.SECRETARY, relation=RELATION.SUGGESTS_CANDIDATE)
# Art. 6a
G.add_edge(ELEMENT.PRIME_MINISTER, ELEMENT.COUNCIL_OF_MINISTERS, relation=RELATION.DEMITS)
# Art. 7 p. 1
G.add_edge(ELEMENT.REPRESENTATIVE, ELEMENT.COMMITTEE, relation=RELATION.IS_MEMBER, may = True)
# Art. 7 p. 3
G.add_edge(ELEMENT.REPRESENTATIVE, ELEMENT.COUNCIL_OF_MINISTERS, relation=RELATION.IS_MEMBER, may = True)
# Art. 7 p. 2 pdp. 2
G.add_edge(ELEMENT.REPRESENTATIVE, ELEMENT.COMMITTEE, relation=RELATION.OBEYS_COMMANDS)
# Art. 7 p. 8 pdp. 4
G.add_edge(ELEMENT.MARSHALL, ELEMENT.REPRESENTATIVE, relation=RELATION.GRANTS_VACATION, may=True)
# Art. 8 p. 1
G.add_edge(ELEMENT.REPRESENTATIVE, ELEMENT.CLUB, relation=RELATION.IS_MEMBER, may = True)
# Art. 8 p. 1
G.add_edge(ELEMENT.REPRESENTATIVE, ELEMENT.CIRCLE, relation=RELATION.IS_MEMBER, may = True)
# Art. 10 p. 1 pdp. 2
G.add_edge(ELEMENT.MARSHALL, ELEMENT.PARLIMENT, relation=RELATION.REPRESENTS)
# Art. 10 p. 1 pdp. 2
G.add_edge(ELEMENT.MARSHALL, ELEMENT.PARLIMENT, relation=RELATION.LEADS)
# Art. 10 p. 1 pdp. 12
G.add_edge(ELEMENT.MARSHALL, ELEMENT.REPRESENTATIVE, relation=RELATION.HELPS)
# Art. 10 p. 1 pdp. 15
G.add_edge(ELEMENT.MARSHALL, ELEMENT.COMMITTEE, relation=RELATION.CONSULTS_WITH)
G.add_edge(ELEMENT.MARSHALL, ELEMENT.PRESIDIUM, relation=RELATION.CONSULTS_WITH)
# Art. 10 p. 1 pdp. 16
G.add_edge(ELEMENT.MARSHALL, ELEMENT.CHIEF_OF_REGISTARS_OFFICE, relation=RELATION.INSTITUTES)
G.add_edge(ELEMENT.MARSHALL, ELEMENT.CHIEF_OF_REGISTARS_OFFICE, relation=RELATION.CANCELS)
# Art. 10 p. 1 pdp. 17
G.add_edge(ELEMENT.MARSHALL, ELEMENT.VICE_CHIEF_OF_REGISTARS_OFFICE, relation=RELATION.INSTITUTES)
G.add_edge(ELEMENT.MARSHALL, ELEMENT.VICE_CHIEF_OF_REGISTARS_OFFICE, relation=RELATION.CANCELS)
# Art. 10 p. 3
G.add_edge(ELEMENT.VICE_MARSHALL, ELEMENT.MARSHALL, relation=RELATION.SUBSTITUTES)
# Art. 10a p. 1
G.add_edge(ELEMENT.PARLIMENT, ELEMENT.MARSHALL, relation=RELATION.CANCELS)
# Art. 10a p. 2
G.add_edge(ELEMENT.PARLIMENT, ELEMENT.MARSHALL, relation=RELATION.INSTITUTES)
# Art. 10a p. 5
G.add_edge(ELEMENT.PARLIMENT, ELEMENT.VICE_MARSHALL, relation=RELATION.CANCELS)
# Art. 11
G.add_edge(ELEMENT.MARSHALL, ELEMENT.PRESIDIUM, relation=RELATION.IS_MEMBER)
G.add_edge(ELEMENT.VICE_MARSHALL, ELEMENT.PRESIDIUM, relation=RELATION.IS_MEMBER)
# Art. 12 pdp. 5
G.add_edge(ELEMENT.PRESIDIUM, ELEMENT.SENIOR_CONVENT, relation=RELATION.CONSULTS_WITH)
# Art. 15 p. 1
G.add_edge(ELEMENT.MARSHALL, ELEMENT.SENIOR_CONVENT, relation=RELATION.IS_MEMBER)
G.add_edge(ELEMENT.VICE_MARSHALL, ELEMENT.SENIOR_CONVENT, relation=RELATION.IS_MEMBER)
G.add_edge(ELEMENT.CHIEF_OF_CLUB, ELEMENT.SENIOR_CONVENT, relation=RELATION.IS_MEMBER)
G.add_edge(ELEMENT.VICE_CHIEF_OF_CLUB, ELEMENT.SENIOR_CONVENT, relation=RELATION.IS_MEMBER)
# Art. 18 p. 3
G.add_edge(ELEMENT.MARSHALL, ELEMENT.COMMITTEE, relation=RELATION.DECIDES_BUDGET)
# Art. 19 p. 1
G.add_edge(ELEMENT.PARLIMENT, ELEMENT.SPECIAL_COMMITTEE, relation=RELATION.INSTITUTES)
G.add_edge(ELEMENT.PARLIMENT, ELEMENT.SPECIAL_COMMITTEE, relation=RELATION.CANCELS)
# Art. 19a
G.add_edge(ELEMENT.PARLIMENT, ELEMENT.FORENSIC_COMMITTEE, relation=RELATION.INSTITUTES)
# Art. 20 p. 1
G.add_edge(ELEMENT.PARLIMENT, ELEMENT.COMMITTEE, relation=RELATION.CHOOSES)
# Art. 20 p. 2
G.add_edge(ELEMENT.CHIEF_OF_COMMITTEE, ELEMENT.COMMITTEE, relation=RELATION.IS_MEMBER)
G.add_edge(ELEMENT.VICE_CHIEF_OF_COMMITTEE, ELEMENT.COMMITTEE, relation=RELATION.IS_MEMBER)
# Art. 20 p. 3
G.add_edge(ELEMENT.COMMITTEE, ELEMENT.PRESIDIUM, relation=RELATION.CHOOSES)
G.add_edge(ELEMENT.COMMITTEE, ELEMENT.PRESIDIUM, relation=RELATION.CANCELS)
# Art. 21 p. 1
G.add_edge(ELEMENT.PRESIDIUM, ELEMENT.REPRESENTATIVE, relation=RELATION.WARN, may = True)
# Art. 23 p. 1
G.add_edge(ELEMENT.PRESIDIUM, ELEMENT.REPRESENTATIVE, relation=RELATION.DECREASE_DIET, may = True)
# Art. 24 p. 1
G.add_edge(ELEMENT.MARSHALL, ELEMENT.REPRESENTATIVE, relation=RELATION.DECREASE_DIET, may = True)
# Art. 25 p. 1
G.add_edge(ELEMENT.MARSHALL, ELEMENT.REPRESENTATIVE, relation=RELATION.EXCLUDE_FROM_PRECEEDINGS, may = True)


# Drawing the graph
FILE_NAME = "RelationGraph"
GRAPH_IMAGE_SIZE = (40,40)
fig = plt.figure(figsize=GRAPH_IMAGE_SIZE)
edge_labels = nx.get_edge_attributes(G,'relation')
pos = nx.planar_layout(G)
nx.draw_networkx_edge_labels(G, pos, edge_labels)
nx.draw(G, pos, with_labels = True)
plt.savefig(FILE_NAME + ".svg", format="SVG")
plt.savefig(FILE_NAME + ".png", format="PNG")
plt.show()