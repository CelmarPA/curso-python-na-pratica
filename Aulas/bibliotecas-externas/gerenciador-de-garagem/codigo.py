import json
from json import JSONDecodeError
from tabulate import tabulate


def ler_carros_arquivos():
    try:
        with open("carros.json", "r") as arquivo_json:
            lista_convertida = json.load(arquivo_json)
            return lista_convertida

    except FileNotFoundError:
        print("Primeira execução. Arquivo vazio.")

        lista_convertida = []
        
        return lista_convertida
    
    except JSONDecodeError:
        print("Conteúdo do arquivo não pode ser convertido.")

        lista_convertida = []
        
        return lista_convertida


def salvar_carros():
    with open("carros.json", "w") as arquivo_json:
        json.dump(carros, arquivo_json, indent=2)


carros = ler_carros_arquivos()


def encontrar_carro(placa):
    carro_encontrado = None

    for carro in carros:
        if carro["placa"].lower() == placa.lower():
            carro_encontrado = carro
            break

    return carro_encontrado


def cadastrar_carro():
    placa = input("Digite a placa: ").strip()

    if len(placa) == 0:
        print("\nO campo placa não pode ser vazio!")

        return

    carro_existente = encontrar_carro(placa)

    if carro_existente != None:
        print("\nJá existe um carro cadastrado com essa placa!")

        return

    cor = input("Digite a cor: ").strip()

    if len(cor) == 0:
        print("\nO campo cor não pode ser vazio!")

        return
    
    modelo = input("Digite o modelo: ").strip()

    if len(modelo) == 0:
        print("\nO campo modelo não pode ser vazio!")

        return

    try:
        ano = int(input("Digite o ano: "))

    except ValueError:
        print("\nAno inválido. Digite apenas números.")
        return

    carro = {
        "placa": placa,
        "cor": cor,
        "modelo": modelo,
        "ano": ano
    }

    carros.append(carro)

    salvar_carros()

    print("\nCarro cadastrado com êxito!")


def exibir_carros_lista():
    if len(carros) == 0:
        print("\nNenhum carro cadastrado.")
        return

    print("\n--------------------- LISTA DE CARROS ---------------------")

    for carro in carros:
        print(f"Placa: {carro['placa']} | Modelo: {carro['modelo']} | Cor: {carro['cor']} | Ano: {carro['ano']}")

    print ("-" * 59)


def exibir_carros_tabela():
    if len(carros) == 0:
        print("\nNenhum carro cadastrado.")
        return

    print("\n--------------------- TABELA DE CARROS ---------------------")

    tabela = tabulate(carros, headers="keys", tablefmt="fancy_grid")

    print(tabela, "\n")

    print ("-" * 59)


def editar_carro():
    placa = input("Digite a placa do carro a ser editado: ").strip()

    carro_existente = encontrar_carro(placa)

    if carro_existente == None:
        print("\nNão foi encontrado um carro com essa placa!")

        return
    
    dicionario_atualizacao = {
        "placa": carro_existente["placa"],
        "cor": carro_existente["cor"],
        "modelo": carro_existente["modelo"],
        "ano": carro_existente["ano"]
    }
    
    print("\nPressione Enter para manter o valor atual.")

    nova_placa = input(f"Nova placa (atual: {carro_existente['placa']}): ").strip()

    if len(nova_placa) > 0 and nova_placa.lower() != carro_existente["placa"]:
        if encontrar_carro(nova_placa) != None:
            print("\nJá existe um outro carro com essa placa!")

            return
        
        dicionario_atualizacao["placa"] = nova_placa

    nova_cor = input(f"Nova cor (atual: {carro_existente['cor']}): ").strip()

    if len(nova_cor) > 0:
        dicionario_atualizacao["cor"] = nova_cor

    novo_modelo = input(f"Novo modelo (atual: {carro_existente['modelo']}): ").strip()

    if len(novo_modelo) > 0:
        dicionario_atualizacao["modelo"] = novo_modelo

    novo_ano = input(f"Novo ano (atual: {carro_existente['ano']}): ")

    if len(novo_ano) > 0:
        try:
            dicionario_atualizacao["ano"] = int(novo_ano)
        
        except ValueError:
            print("\nAna inválido. Alterações ignoradas.")
            return

    carro_existente["placa"] = dicionario_atualizacao["placa"]
    carro_existente["cor"] = dicionario_atualizacao["cor"]
    carro_existente["modelo"] = dicionario_atualizacao["modelo"]
    carro_existente["ano"] = dicionario_atualizacao["ano"]

    salvar_carros()

    print("\nCarro atualizado com êxito!")

    # carro_existente.update(dicionario_atualizacao) # Update atualiza tudo de uma vez.


def deletar_carro():
    placa = input("Digite a placa do carro a ser deletado: ").strip()

    carro_retornado = encontrar_carro(placa)

    if carro_retornado == None:
        print("\nNão foi encontrado um carro com essa placa!")
        
        return

    carros.remove(carro_retornado)
    salvar_carros()

    print("\nCarro deletado com êxito!")


def exibir_menu():
    print("\n---------- GERENCIADOR DE GARAGEM ----------")
    print("1 - Cadastrar um carro")
    print("2 - Exibir os carros existentes (lista)")
    print("3 - Exibir os carros existentes (tabela)")
    print("4 - Editar um carro")
    print("5 - Deletar um carro")
    print("6 - Sair")


while True:
    exibir_menu()

    opcao_escolhida = input("Escolha uma opção: ").strip()

    print(f"A opção escolhida foi '{opcao_escolhida}'")

    if opcao_escolhida == "1":
        cadastrar_carro()

    elif opcao_escolhida == "2":
        exibir_carros_lista()

    elif opcao_escolhida == "3":
        exibir_carros_tabela()
        
    elif opcao_escolhida == "4":
        editar_carro()

    elif opcao_escolhida == "5":
        deletar_carro()

    elif opcao_escolhida == "6":
        print("\nEncerrando o gerenciador de garagem. Até mais!")

        break

    else:
        print("\nOpção inválida. Tente novamente!")

        continue
