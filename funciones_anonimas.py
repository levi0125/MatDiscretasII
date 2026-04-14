"""
    ================= lambda =================
"""
# Funciones pequeñas sin nombre...
suma = lambda x,y : x+y
resultado = suma(3,4)
print(f"{resultado=}")


"""
    ================= MAP =================
"""
# Aplica una transformacion lambda a cada elemento d euna lista. (es un iterador de elementos)
resultado = list(map(lambda x: x**2, [1,2,3,4,5]))
print(f"{resultado=}")


"""
    ================= FILTER =================
"""
# Apica una condicion lambda para filtrar elementos
numeros = [x for x in range(1,11)] # numeros del 1 al 10
# Encuentra numeros impares en la lista
resultado = list(filter(lambda x: x%2 != 0, numeros))
print(f"{resultado=}")

"""
    ================= REDUCE =================
"""

import functools
suma = lambda x,y : x+y
numeros = [1,2,3,4,5]
resultado = functools.reduce(suma,numeros,0)
print(f"{resultado=}")