def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    return a / b


def menu():
    print(f"\n=== CALCULADORA ===\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n0 - Sair")


resultado_atual = float(input("Digite um valor inicial: "))

while True:
    print(f"Resultado atual: {resultado_atual}")
    menu()

    opcao = input("Escolha uma operação: ")

    if opcao == "0":
        break

    elif opcao not in ["0", "1", "2", "3", "4"]:
        print(f"\nOperação inválida!\n")
        continue
    
    valor_operando = float(input("Digite o próximo valor: "))

    if opcao == "1":
        resultado_atual = soma(resultado_atual, valor_operando)

    elif opcao == "2":
        resultado_atual = subtracao(resultado_atual, valor_operando)
    
    elif opcao == "3":
        resultado_atual = multiplicacao(resultado_atual, valor_operando)
    
    elif opcao == "4":
        resultado_atual = divisao(resultado_atual, valor_operando)


print(f"Encerrando a calculadora. Até mais!")