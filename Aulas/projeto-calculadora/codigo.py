def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    return a / b


def exibir_menu():
    print(f"\n=== CALCULADORA ===")
    print(f"1 - Soma")
    print(f"2 - Subtração")
    print(f"3 - Multiplicação")
    print(f"4 - Divisão")
    print(f"0 - Sair")

def formatar_resultado(resultado):
    if resultado.is_integer():
        resultado_convertido = int(resultado)

        return  resultado_convertido

    return resultado

def main():

    opcoes_validas = {"0", "1", "2", "3", "4"}

    try:
        resultado_atual = float(input("Digite um valor inicial: "))

    except ValueError:
        print("Valor inicial inválido!")
        return

    while True:
        resultado_formatado = formatar_resultado(resultado_atual)
        print(f"Resultado atual: {resultado_formatado }")
        exibir_menu()

        opcao_escolhida = input("Escolha uma operação: ")

        if opcao_escolhida == "0":
            break

        if opcao_escolhida not in opcoes_validas:
            print("\nOpção inválida!")
            print("Opções válidas: 1, 2, 3, 4 e 0\n")

            continue
        
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

    print(f"\nEncerrando a calculadora. Até mais!")

if __name__ == "__main__":
    main()
