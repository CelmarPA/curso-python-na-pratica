dicionario = {
    "nome": "Celmar",
    "estado": "Minas Gerais",
    "altura": 1.84
}

print(f"Tipo do dicionário: {type(dicionario)}")

print("Dicionário antes da modificação")
print(dicionario)

dicionario["nome"] = "Dev Celmar"
dicionario["linguagem"] = "Python"

print("Dicionário após a modificação")
print(dicionario)

print(dicionario["nome"])
print(dicionario["estado"])
