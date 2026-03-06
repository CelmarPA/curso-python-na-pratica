from datetime import date
from playsound3 import playsound



media = float(input("Média do aluno: "))

if media >= 7.0:
    print("Passou direto!")

    playsound("efeito-sonoro/tadam.mp3")

elif (media >= 4.0) and (media < 7.0):
    print("Recuperação")

    data_prazo = date(2026, 1, 31)

    dia = data_prazo.day
    mes = data_prazo.month
    ano = data_prazo.year

    print(f"Prazo para prova de recuperação: {dia}/{mes}/{ano}")

    formato_data = "%d/%m/%Y"

    while True:
        try:
            data_prova_str = input("Quando o aluno fez a prova? (dd/mm/aaaa): ").strip()
            data_prova_date = date.strptime(data_prova_str, formato_data)
            
            break

        except ValueError:
            print("Formato de data inválido. Use dd/mm/aaaa")


    if data_prova_date <= data_prazo:
        nota_rec = float(input("Nota de recuperação: "))

        if nota_rec >= 7.0:
            print("Passou na recuperação.")

            playsound("efeito-sonoro/tadam.mp3")

        else:
            print("Reprovou na recuperação.")

    else:
        print("Prova feita fora do prazo. Aluno reprovado!")

else:
    print("Reprovou direto.")
