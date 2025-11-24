numero = int(input("Informe um número [zero para sair]: "))

somatorio = 0

while numero != 0:
    somatorio += numero
    numero = int(input("Informe mais um número [zero para sair]: "))
    

print(f"O somatório dos número informados é igual a: {somatorio}")
