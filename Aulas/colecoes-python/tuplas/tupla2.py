tupla = (10, 20, 30)
print(f"Tipo da tupla: {type(tupla)}")

lista_convertida = list(tupla)
print(f"Tipo da lista convertida: {type(lista_convertida)}")

lista_convertida[1] = 2000

tupla_convertida = tuple(lista_convertida)

print(f"Tipo da tupla convertida: {type(tupla_convertida)}")
print(tupla_convertida)
