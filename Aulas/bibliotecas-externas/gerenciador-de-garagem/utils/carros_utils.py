def encontrar_carro(placa, lista_carros):
    carro_encontrado = None

    for carro in lista_carros:
        if carro["placa"].lower() == placa.lower():
            carro_encontrado = carro
            break

    return carro_encontrado
