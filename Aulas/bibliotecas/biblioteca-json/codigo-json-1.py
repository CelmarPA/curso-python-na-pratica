import json

pessoa = {
    "nome": "Gustavo",
    "idade": 20,
    "email": "gustavo@cdc.com",
    "desenvolvedora": True
}

print(f"Tipo da pessoa: {type(pessoa)}\n")

json_equivalente = json.dumps(pessoa, indent=2)

print(json_equivalente)

print(f"Tipo do json equivalente (conversão): {type(json_equivalente)}")
