import json

with open("pessoa.json", "r") as arquivo_json:
    dict_convertido = json.load(arquivo_json)

    print(dict_convertido)

    print(type(dict_convertido))

print(dict_convertido["altura"])

print(type(dict_convertido["linguagens"]))
