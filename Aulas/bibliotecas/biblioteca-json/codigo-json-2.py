import json

json_input = '{"nome": "Isaac", "idade": 20, "email": "isaac@email.com"}'

print(f"Tipo do input: {type(json_input)}\n")

dict_convertido = json.loads(json_input)

print(dict_convertido)

print(f"Tipo do dict convertido: {type(dict_convertido)}")

print(dict_convertido["nome"])
