from datetime import date

data = date(2026, 12, 10)

if data.day == 25 and data.month == 12:
    print("É natal!")

else:
    print("Não é natal!")
    