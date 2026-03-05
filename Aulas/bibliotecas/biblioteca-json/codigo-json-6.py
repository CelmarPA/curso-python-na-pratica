import json

lista_dicts = [
    {
        "nome": "Daniel",
        "idade": 50,
        "altura": 1.76,
        "dev": True,
        "linguagens": ["Python", "Java", "Go"]
    },
    {
        "nome": "Daniel",
        "idade": 50,
        "altura": 1.76,
        "dev": True,
        "linguagens": ["Python", "Java", "Go"]
    },
    {
        "nome": "Daniel",
        "idade": 50,
        "altura": 1.76,
        "dev": True,
        "linguagens": ["Python", "Java", "Go"]
    },
]

# print(f"Tipo da lista: {type(lista_dicts)}")

# for item in lista_dicts:
#     print(f"Tipo do item:{type(item)}")

json_str = json.dumps(lista_dicts,  indent=2)

print(json_str)
print(type(json_str))
