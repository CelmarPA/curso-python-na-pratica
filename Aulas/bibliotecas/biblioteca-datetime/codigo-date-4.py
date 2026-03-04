from datetime import date

data_1 = date(2026, 1, 10)
data_2 = date(2026, 1, 4)

print(data_1)
print(type(data_1))
print(data_2)
print(type(data_2))

if data_1 < data_2:
    print("Data 1 é antes de data 2")

elif data_1 > data_2:
    print("Data 1 é depois de data 2")

else:
    print("Data 1 e data 2 são iguais")
