from datetime import date

# strptime
data_string = "20/06/2025"
data_formato = "%d/%m/%Y"

# print(type(data_string))

data_date = date.strptime(data_string, data_formato)

print(data_date)
print(type(data_date))

print(f"Mês anterior ao mês da data: {data_date.month - 1}")