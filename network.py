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
    VICECHIEF_OF_REGISTARS_OFFICE = "zastępca szefa kancelarii sejmu"
    SENIOR_CONVENT = "konwent seniorów"
    CHIEF_OF_CLUB = "przewodniczący klubu"
    VICE_CHIEF_OF_CLUB = "wiceprzewodniczący klubu"
    SPECIAL_COMMITTEE = "komisja nadzwyczajna"
    FORENSIC_COMMITTEE = "komisja śledcza"
    
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
    REPRESENTS = "reprezentuje"
    LEADS = "przewodzi"
    HELPS = "udziela pomocy"
    CONSULTS_WITH = "konsultuje się z"
    SUBSTITUTES = "zastępuje"
    DECIDES_BUDGET = "decyduje o budżecie"

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
G.add_edge(ELEMENT.MARSHALL, ELEMENT.VICE_MARSHALL, relation=RELATION.COMMANDS_CHOICE)
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
G.add_edge(ELEMENT.PARLIMENT, ELEMENT.SPECIAL_COMMITTEE, relation=RELATION.INTITUTES)
G.add_edge(ELEMENT.PARLIMENT, ELEMENT.SPECIAL_COMMITTEE, relation=RELATION.CANCELS)
# Art. 19a
G.add_edge(ELEMENT.PARLIMENT, ELEMENT.FORENSIC_COMMITTEE, relation=RELATION.INTITUTES)

# Drawing the graph
edge_labels = nx.get_edge_attributes(G,'relation')
pos = nx.planar_layout(G)
nx.draw_networkx_edge_labels(G, pos, edge_labels)
nx.draw(G, with_labels = True)
plt.show()
