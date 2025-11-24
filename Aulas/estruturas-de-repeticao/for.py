# somatório = 0
# sequencia: [1, 2, 3, 4, 5]
# i = 1
# somatório = 0 + 1 -> 1
# i = 2
# somatório = 1 + 2 -> 3
# i = 3
# somatório = 3 + 3 -> 6
# i = 4
# somatório = 6 + 4 -> 10
# i = 5
# somatório = 10 + 5 -> 15

somatorio = 0
for i in range(1, 6):
    print(f"Executando pela {i}ª vez")
    somatorio = somatorio + i
    # somatorio += i
    # somatorio = somatorio - 1
    # somatorio -= i

print(f"Somatório dos números: {somatorio}")
print("Acabou o loop.")
