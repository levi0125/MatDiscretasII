import re
# 1. Añadir cadenas a 'comal' y valiar que no sean espacios ni conjuntos vacios

c = "Comal"
n = len(c)
while True:
    cad = input("Valor a concatenar:")
    if(re.match(r'[a-zA-Z]{1,}$',cad)==None):
        print("Ingresaste caracteres invalidos(solo se aceptan caracteres del alfabeto latino). Intenta de nuevo")
    else:
        break

concatenado = c+cad
print("Palabra concatenada:", concatenado)
print("\tlongitud:",len(concatenado))



# 2. Listar las veces que aparece cada letra de una palabra
palabra = "malvavisco"
letras = {}
for letra in palabra:
    letras[letra] = letras.get(letra,0)+1

for llave, valor in letras.items():
    print(f"\t{llave}:{valor}")