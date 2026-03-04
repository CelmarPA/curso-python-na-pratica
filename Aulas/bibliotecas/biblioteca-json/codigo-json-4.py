import json

pessoa = {
    "nome": "Daniel",
    "idade": 50,
    "altura": 1.76,
    "dev": True,
    "linguagens": ["Python", "Java", "Go"]
}

with open("pessoa.json", "w") as arquivo_json:
    json.dump(pessoa, arquivo_json, indent=2)

print("Terminamos de gravar o arquivo")

# Primeiro transforma em string
# Depois escreve no arquivo
# Útil se você quiser manipular o JSON como texto antes de salvar
# with open("pessoa.json", "w") as arquivo_json:
#     arquivo_json.write(json.dumps(pessoa, indent=2))