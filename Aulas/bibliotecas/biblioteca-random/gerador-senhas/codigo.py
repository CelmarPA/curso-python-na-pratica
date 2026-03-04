import string
from random import choice, shuffle

lista_letras = list(string.ascii_lowercase + string.ascii_uppercase)
lista_numeros = list(string.digits)
lista_simbolos = list(string.punctuation)

qtd_letras = int(input("Quantas letras você quer na sua senha? "))
qtd_numeros = int(input("Quantos numeros você quer na sua senha? "))
qtd_simbolos = int(input("Quantos simbolos você quer na sua senha? "))

lista_caracteres = []

for _ in range(qtd_letras):
    lista_caracteres.append(choice(lista_letras))

for _ in range(qtd_numeros):
    lista_caracteres.append(choice(lista_numeros))

for _ in range(qtd_simbolos):
    lista_caracteres.append(choice(lista_simbolos))

shuffle(lista_caracteres)

senha_str  = "".join(lista_caracteres)

print(f"Senha aleatória gerada: {senha_str}")