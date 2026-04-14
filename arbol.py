import functools

class Nodo:
	def __init__(self, valor, nivel=1):
		self.valor = str(valor)
		self. izquierda = None
		self. derecha = None
		self.nivel = nivel
		
	def setHijos(self,izq=None,der=None):
		self. izquierda = izq
		self. derecha = der

		return self

	def set_nivel_hijos(self,nivel,direccion=None):
		if(self.izquierda==None and self.derecha==None):
			return nivel-1
		
		fondo = 0
		if(self.izquierda!=None):
			self.izquierda.nivel = nivel
			fondo = self.izquierda.set_nivel_hijos(nivel+1)
		
		if(self.derecha!=None):
			self.derecha.nivel = nivel
			fondo = max(fondo,self.derecha.set_nivel_hijos(nivel+1))
	
		return fondo
	def __str__(self):
		return f"[{self.nivel}]{self.valor}"

class ArbolBinario:
	niveles=[]
	orden_valores = []
	fondo = None
	padres = {}
	lambda_max_longitud = lambda self,longitud_actual, otra_longitud: max(longitud_actual, len(str(otra_longitud)))

	def __init__(self,raiz):
		self.raiz = Nodo(raiz)
	
	def agregar_hijos(self,izquierda, derecha):
		self.raiz.setHijos(izquierda,derecha)

		fondo = self.raiz.set_nivel_hijos(2)
		self.fondo = fondo
		self.niveles = [[] for x in range (fondo)]

	def resetear_datos(self):
		for x in range (len(self.niveles)):
			self.niveles[x]=[]

		self.padres={}
		
	def imprimir_arbol(self):
		"""
			Codigo para dibujar el grafo
			___ 1 | 2 | 3 | AB |
		"""
		self.resetear_datos()
		in_order=self.recorrido_inorder()
		NUMERO_NODOS = len(in_order)
		ANCHO_COLUMNA = functools.reduce( self.lambda_max_longitud, in_order, 0) + 3
		CADENA_UNION = "|"

		print(" ARBOL ".center((ANCHO_COLUMNA+1)*(NUMERO_NODOS) -1,"="))
		molde_renglon = [" "*ANCHO_COLUMNA for x in range(NUMERO_NODOS) ]
		posiciones={}
		for nivel in self.niveles:
			renglon = molde_renglon.copy()
			for nodo in nivel:
				posicion_nodo = in_order.index(nodo)
				prefijo,sufijo = "",""
				
				posiciones[nodo] = posicion_nodo
				es_raiz = self.padres.get(nodo,"r")=="r"
				if(not es_raiz):
					posicion_padre = posiciones.get(self.padres[nodo],0)

					if(posicion_padre < posicion_nodo):
						prefijo = "\\"
					else:
						sufijo = "/"
				else:
					prefijo="^"
				renglon[posicion_nodo] = f"{prefijo}{nodo}{sufijo}".center(ANCHO_COLUMNA)
			print(CADENA_UNION.join(renglon))
	
	def __analisis_inorder(self,nodo:Nodo, orden = [], padre_v=None):
		if(nodo==None):
			return
		self.niveles[nodo.nivel-1].append(nodo.valor)
		
		self.__analisis_inorder(nodo.izquierda, orden, padre_v=nodo.valor)
		self.padres[nodo.valor] = padre_v
		orden.append(nodo.valor)
		self.__analisis_inorder(nodo.derecha, orden, padre_v=nodo.valor)

	def recorrido_inorder(self):			
		nodo = self.raiz
		orden = []

		self.__analisis_inorder(nodo,orden,"r")
		return orden

"""
	Arbol 1
"""
arbol = ArbolBinario(1)

arbol.agregar_hijos( 
	Nodo(2).setHijos(
		Nodo(4),
		Nodo(5).setHijos(
			Nodo(8),
			None
		)		
	), 
	Nodo(3).setHijos(
		Nodo(6),
		Nodo(7).setHijos(
			None,
			Nodo(9)
		)
	)
)

arbol.imprimir_arbol()
###
###	Arbol 2
###
arbol2 = ArbolBinario("A")
arbol2.agregar_hijos( 
	Nodo("B").setHijos(
		Nodo("D"),
		Nodo("E")
	), 
	Nodo("C").setHijos(
		None,
		Nodo("F").setHijos(
			Nodo("G"),
			Nodo("H")
		)
	)
)
arbol2.imprimir_arbol()