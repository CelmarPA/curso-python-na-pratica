limite = int(input("Informe um limite: "))

produtorio = 1

for i in range(1, limite + 1):
    produtorio *= i

print(f"O produtório para o limite {limite} é igual a: {produtorio}")