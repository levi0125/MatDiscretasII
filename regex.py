import re

# # 1. Entrada del alfabeto
# alfabeto = input("Ingresa el alfabeto separado por comas: ").split(',')

# # 2. Cadena
# cadena = input("Ingresa una cadena de longitud 8: ")

# # 3. Validar longitud
# if len(cadena) != 8:
#     print("Error: la cadena debe tener 8 caracteres")
#     exit()

# # 4. Validar símbolos
# for c in cadena:
#     if c not in alfabeto:
#         print("Error: símbolo no válido:", c)
#         exit()

# # 5. Expresión regular
# expresion = r"[a-zA-Z][a-zA-Z0-9]{6}[0-9]"

# # 6. Validación
# if re.fullmatch(expresion, cadena):
#     print("Cadena válida según la expresión regular")
# else:
    # print("Cadena inválida")

regex=r"c+(a|b|c){1,}"
cad="caad"

print(True if re.search(regex, cad) is not None else False)

# c(a|b|c)^*