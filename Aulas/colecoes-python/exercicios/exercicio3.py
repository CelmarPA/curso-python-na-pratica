lista = [2, 3, 5, 3, 6, 7, 7, 8, 1, 2, 9, 2]

print("Lista original")
print(lista)

conjunto_convertida = set(lista)

print(f"Tipo do conjunto convertido: {type(conjunto_convertida)}")
print(conjunto_convertida)

lista_convertida = list(conjunto_convertida)

print(f"Tipo da lista convertida: {type(lista_convertida)}")

print(lista_convertida)
