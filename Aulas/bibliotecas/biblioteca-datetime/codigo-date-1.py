from datetime import date

# sequencia: ano, mes, dia
minha_data = date(2026, 9, 7)

print(minha_data)
print(type(minha_data))

print(f"Dia da data: {minha_data.day}")
print(f"Mês da data:{minha_data.month}")
print(f"Ano da data: {minha_data.year}")
