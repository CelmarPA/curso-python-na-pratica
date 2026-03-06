from math import sqrt, log2
from termcolor import colored


def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    return a / b


def raiz_quadrada(a):
    return sqrt(a)


def logaritmo(a):
    return log2(a)


def exibir_menu():
    print(f"\n=== CALCULADORA ===")
    print(f"1 - Soma")
    print(f"2 - Subtração")
    print(f"3 - Multiplicação")
    print(f"4 - Divisão")
    print(f"5 - Raiz Quadrada (do resultado atual)")
    print(f"6 - Logaritmo Base 2 (do resultado atual)")
    print(f"0 - Sair")


def formatar_resultado(resultado):
    if resultado.is_integer():
        resultado_convertido = int(resultado)

        return  resultado_convertido

    return resultado


def colorir_resultado(resultado_formatado):
    cor_resultado = ""

    if resultado_formatado >= 0:
        cor_resultado = "green"

    else:
        cor_resultado = "red"

    resultado_colorido = colored(resultado_formatado, cor_resultado)

    return resultado_colorido


def main():

    opcoes_validas = {"0", "1", "2", "3", "4", "5", "6"}

    try:
        resultado_atual = float(input("Digite um valor inicial: "))

    except ValueError:
        print("Valor inicial inválido!")
        return

    while True:
        resultado_formatado = formatar_resultado(resultado_atual)
        resultado_colorido = colorir_resultado(resultado_formatado)

        print(f"Resultado atual: {resultado_colorido}")
        exibir_menu()

        opcao_escolhida = input("Escolha uma operação: ")

        if opcao_escolhida == "0":
            break

        if opcao_escolhida not in opcoes_validas:
            print("\nOpção inválida!")
            print("Opções válidas: 1, 2, 3, 4, 5, 6 e 0\n")

            continue
        
        if opcao_escolhida in {"1", "2", "3", "4"}:
            try:
                    valor_operando = float(input("Digite o próximo valor do operando: "))

            except ValueError:
                print("Número inválido!")

                continue

        if opcao_escolhida == "1":
            resultado_atual = soma(resultado_atual, valor_operando)

        elif opcao_escolhida == "2":
            resultado_atual = subtracao(resultado_atual, valor_operando)
        
        elif opcao_escolhida == "3":
            resultado_atual = multiplicacao(resultado_atual, valor_operando)
        
        elif opcao_escolhida == "4":
            try:
                resultado_atual = divisao(resultado_atual, valor_operando)

            except ZeroDivisionError:
                print("Não se pode dividir por zero.")
        
        elif opcao_escolhida == "5":
            try:
                resultado_atual = raiz_quadrada(resultado_atual)

            except ValueError:
                print("Não é possível calcular raiz quadrada de um número negativo.")

        elif opcao_escolhida == "6":
            try:
                resultado_atual = logaritmo(resultado_atual)

            except ValueError:
                print("Logaritmo só é definido para números positivos e diferentes de zero.")


    print(f"\nEncerrando a calculadora. Até mais!")


if __name__ == "__main__":
    main()
