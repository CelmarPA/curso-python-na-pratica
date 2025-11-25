paises = ["Brazil", "Paraguai", "Japão", "China"]

print("Lista original")
print(paises)


paises.append("Russia")

print("Após adicionar Russia")
print(paises)

paises.insert(1, "França")

print("Após adicionar França")
print(paises)

paises.remove("China")

print("Após remover China")
print(paises)

paises.pop(2)

print("Após remover país do índice 2")
print(paises)

tam = len(paises)

print(f"O total de países na lista é de {tam} países.")
