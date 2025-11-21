temperatura = float(input("Digite a temperatura atual: "))

if temperatura >= 30:
    print("Está muito quente!")

elif temperatura >= 20 and temperatura < 30:
    print("Está agradável!")

else:
    print("Está muito frio!")
