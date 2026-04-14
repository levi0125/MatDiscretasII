from colorama import Back
from InsercionBinaria import OrdenamientoBinario
class Grafo:
	# max_largo_nodo = 1
	ob = None
	nodos_ordenados = []
	orden_aristas = []

	def __init__(self, es_dirigido=False, ordernar_nodos=True, lista_nodos=None, lista_aristas=None):
		self.es_dirigido = es_dirigido
		self.ordernar_nodos = ordernar_nodos

		if(lista_aristas!=None):
			self.set_aristas(lista_aristas)
		if(lista_nodos!=None):
			self.set_lista_nodos(lista_nodos)

	def set_lista_nodos(self,nodos):
		self.lista_nodos = nodos
		self.n_nodos = len(nodos)
		ob = OrdenamientoBinario()
		if(self.ordernar_nodos==True):
			self.nodos_ordenados = ob.ordenar_lista(self.lista_nodos)
		#self.deducir_max_longitud_nodo(nodos)
	
	def deducir_max_longitud_nodo(self,nodos):
		nodos_son_enteros = type(nodos[0]) == int
		nodos_son_strings = type(nodos[0]) == str

		if(nodos_son_enteros or (nodos_son_strings and nodos[0].isdigit()) ):
			return len(str(max(nodos)))
		elif (nodos_son_strings):
			return max([len(x) for x in nodos] )
		
	def deducir_min_longitud_nodo(self,nodos):
		nodos_son_enteros = type(nodos[0]) == int
		nodos_son_strings = type(nodos[0]) == str

		if(nodos_son_enteros or (nodos_son_strings and nodos[0].isdigit()) ):
			return len(str(min(nodos)))
		elif (nodos_son_strings):
			return min([len(x) for x in nodos] )

	def set_aristas(self,lista_aristas):
		self.lista_aristas = lista_aristas
		self.n_aristas = len(lista_aristas)
		
		self.set_lista_nodos(self.deducir_nodos(lista_aristas))
		
	def deducir_nodos(self,lista_aristas):
		vertices= {}
		for arista in lista_aristas:
			for nodo in arista:
				vertices[nodo] = 1
		return list(vertices.keys())
	
	def imprimir_matriz_2(self,matriz,titulo, lista_encabezados):
		"""
			max_largo_nodo = 1 ->
				$1$,$2$,$3$,...$9$
			max_largo_nodo = 2 ->
				11,12,13,14
		"""
		max_largo_nodo = self.deducir_max_longitud_nodo(self.lista_nodos)
		min_largo_titulo = max(self.deducir_min_longitud_nodo(lista_encabezados),1)
		# espaciado_encabezado = "$" if max_largo_nodo%2 ==1 else ""

		nodos = None
		if(self.ordernar_nodos==True):
			nodos = self.nodos_ordenados
		else:
			nodos = self.lista_nodos

		print(f"===={titulo}====")
		tit = (' |'.join(str(n) for n in lista_encabezados)).replace("|","| ")
		print(f"{' '*(max_largo_nodo+3)} [ {tit} ]")		

		for (index, x) in enumerate(nodos):
			# print("X=",x)
			columna = matriz[x]
			print(f"{str(x).center(max_largo_nodo," ")} -> [{' '*(min_largo_titulo-1)}{f' {Back.RESET}{' '*(max(min_largo_titulo-1,1))}|'.join(columna).replace("|",f"|{' '*(min_largo_titulo-1)}")} {Back.RESET} ]")
			print(f"{' '*(max_largo_nodo+4)}{'-'*(len(tit)+4)}")

	def crear_matriz_adyacencia(self):	
		# matriz = [ 
		# 	[' '*(len(f"{self.lista_nodos[y]}")) for y in range(self.n_nodos)] for x in range (self.n_nodos)
		# ]
		matriz = {}
		for nodo in (self.lista_nodos):
			matriz[nodo]=[' '*len(f"{y+1}") for y in range(self.n_nodos)]
		
		# auste_index = 1
		# if(str(self.nodos_ordenados[0])=="0"):
		# 	ajuste_index = 0
		nodos=None
		if(self.ordernar_nodos==True):
			nodos = self.nodos_ordenados
		else:
			nodos = self.lista_nodos

		for arista in self.lista_aristas:
			l1 = len(f"{arista[0]}")
			l2 = len(f"{arista[1]}")
			
			# print(f"{arista[0]} x {arista[1]}")
			index_y = nodos.index(int(arista[1]))

			matriz[arista[0]][index_y] = f"{Back.RED}1".center(l2+5," ")
			
			if(not self.es_dirigido):
				index_y2 = nodos.index(int(arista[0]))
				matriz[arista[1]][index_y2] = f"{Back.RED}1".center(l1+5," ")
		# print("Nodos ordenados = ",self.nodos_ordenados)
		self.imprimir_matriz_2(matriz,"Lista de Adyacencia", self.nodos_ordenados if self.ordernar_nodos==True else self.lista_nodos)
		return matriz
	
	def crear_matriz_incidencia(self):
		# matriz = [ 
		# 	[' '*len(f"{y+1}") for y in range(self.n_aristas)] for x in range (self.n_nodos)
		# ]

		matriz = {}
		for nodo in (self.lista_nodos):
			matriz[nodo]=[' '*len(f"{y+1}") for y in range(self.n_aristas)]

		# print(matriz)
		for (index,arista) in enumerate(self.lista_aristas):
			# print(f"{arista=}")
			
			longitud = len(f"{index+1}")
			matriz[arista[0]][index] = f"{Back.GREEN}1".center(longitud+5," ")
			matriz[arista[1]][index] = f"{Back.GREEN}1".center(longitud+5," ")

		# print("MATRIZ=",matriz)
		# for m in matriz:
		# 	print(m)

		self.imprimir_matriz_2(matriz,"Lista de Incidencia",[f"e{x}" for x in range(1,self.n_aristas+1)])
		return matriz
	
	def imprimir_matrices(self):
		print("=======Inicio del Grafo======")
		self.crear_matriz_adyacencia()
		self.crear_matriz_incidencia()
		print("========FIN del Grafo========")

lista_aristas = [
	[1,2],
	[2,3],
	[3,4],
	[4,2],
	[4,1],
	[4,7],
	[4,6],
	[4,5],
	[3,7],
	[7,6],
	[6,5],
	[5,1]
]
lista_aristas2 = [
	[0,10],
	[10,1],
	[1,0],
	[0,8],
	[8,1],
	[1,7],
	[1,2],
	[7,2],
	[8,7],
	[8,6],
	[7,5],
	[6,3],
	[2,3],
	[6,4],
	[5,4]
]
Grafo (ordernar_nodos=True,lista_aristas=[
	[1,5],[1,2],
	[5,2],[5,4],
	[2,3],
	[3,4],
	[6,4]]
).imprimir_matrices()

# Grafo(ordernar_nodos=False, lista_nodos=[1,2,3,7,6,5,4], lista_aristas=lista_aristas).imprimir_matrices()
# Grafo(es_dirigido=True,ordernar_nodos=False, lista_nodos=[1,2,3,7,6,5,4], lista_aristas=lista_aristas).imprimir_matrices()
# Grafo(ordernar_nodos=True, lista_aristas=lista_aristas2).imprimir_matrices()