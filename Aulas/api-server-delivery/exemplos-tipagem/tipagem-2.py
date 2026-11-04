def multiplicar_com_tipagem(x: int, y: int) -> int:
    multiplicacao = x * y

    return multiplicacao


resultado = multiplicar_com_tipagem(20, 30)
print(f"Resultado da multiplicação: {resultado}")


resultado_str = multiplicar_com_tipagem("cdc", "dev")
print(f"Resiltado da multiplicação: {resultado_str}")