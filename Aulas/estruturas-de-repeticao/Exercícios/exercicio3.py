# Monte um programa que, para um determinado
# número informado pelo usuário (limite),
# exiba o dobro de cada número de 1 até esse
# limite.

limite = int(input("Informe um limite: "))

for i in range(1, limite + 1):
    print(f"O dobro do número {i} é {i * 2}")