# O Código abaixo repete o mesmo cálculo
# várias vezes.

# Refatore-o, criando um função que leia as 
# notas do aluno, calcule a média,
# retorne-a arredondada com uma casa decimal
# e evite a repetição.

print("Aluno 1:")

nota1 = float(input("Digita a primeira nota: "))
nota2 = float(input("Digita a segunda nota: "))
nota3 = float(input("Digita a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
media = round(media, 1)

print(f"Média do aluno 1: {media}")

print("Aluno 2:")

nota1 = float(input("Digita a primeira nota: "))
nota2 = float(input("Digita a segunda nota: "))
nota3 = float(input("Digita a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
media = round(media, 1)

print(f"Média do aluno 2: {media}")

print("Aluno 3:")

nota1 = float(input("Digita a primeira nota: "))
nota2 = float(input("Digita a segunda nota: "))
nota3 = float(input("Digita a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
media = round(media, 1)

print(f"Média do aluno 3: {media}")
