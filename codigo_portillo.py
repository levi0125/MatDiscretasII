# Definimos los vértices
vertices = ["A", "B", "C", "D", "E", "F"]

# Definimos las aristas
aristas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E"), ("E", "F")]

# Imprimir definición formal
print("G = (V, E)")
print("V =", vertices)
print("E =", aristas)


#Lista de Adyancencia Actualizada
grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D", "F"],
    "F": ["E"]
}

print("\nLista de Adyacencia:")
for vertice in grafo:
    print(vertice, "->", grafo[vertice])

    n = len(vertices)
    
# Definición de un nodo del árbol binario
class Nodo:
    def __init__(self, valor):
        self.valor = valor # Valor del nodo
        self.izquierdo = None # Hijo izquierdo
        self.derecho = None # Hijo derecho

# Definición de un árbol binario
class ArbolBinario:
    def __init__(self, raiz):
        self.raiz = Nodo(raiz) 
        pass
arbol = ArbolBinario(1) 
arbol.raiz.izquierdo = Nodo(2)
arbol.raiz.derecho = Nodo(3)

arbol.raiz.izquierdo.izquierdo = Nodo(4) 
arbol.raiz.izquierdo.derecho = Nodo(5) 

arbol.raiz.derecho.izquierdo = Nodo(6) 
arbol.raiz.derecho.derecho = Nodo(7) 

#Nuevos Nodos 
# Hijos al nodo 4
arbol.raiz.izquierdo.izquierdo.izquierdo = Nodo(8)
arbol.raiz.izquierdo.izquierdo.derecho = Nodo(9)

print("Raíz:", arbol.raiz.valor)
print("Hijo izquierdo de la raíz:", arbol.raiz.izquierdo.valor)
print("Hijo derecho de la raíz:", arbol.raiz.derecho.valor)
