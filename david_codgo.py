import networkx as nx
import matplotlib.pyplot as plt
# Definimos los vértices
vertices = ["A", "B", "C", "D" , "F", "H","G"]

# Definimos las aristas
aristas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "F"), ("F", "H"), ("C", "H")]
aristas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("F", "H"), ("C", "H")]
aristas = [('A','B'),('A','C'),('B','D'),('B','H'),('C','F'),('C','G')]
# Imprimir definición formal
print("G = (V, E)")
print("V =", vertices)
print("E =", aristas)
    
# Crear lista de adyacencia (diccionario o listas)
grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D", "H"], 
    "D": ["B", "C", "F"],
    "F": ["D", "H"],
    "H": ["F", "C"]
}

print("\nLista de Adyacencia:")
for vertice in grafo:
    print(vertice, "->", grafo[vertice])
    
#Construir Grafo
G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(aristas)

pos = {
    "A": (0, 1),
    "B": (-2,0),
    "C": (2,0),
    "D": (-1,-1),
    "H": (-3,-1),
    "F": (1,-1),
    "G": (3,-1)
}
nx.draw(G, pos, with_labels= True)
plt.show()
