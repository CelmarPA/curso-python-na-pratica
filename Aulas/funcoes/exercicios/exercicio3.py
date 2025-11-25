def notas_aprovadas(lista_notas):

    lista_aprovadas = []

    for nota in lista_notas:
        if nota >= 7:
            lista_aprovadas.append(nota)

    return lista_aprovadas

lista_notas_alunos = [10.0, 4.5, 7.5, 9.0]

lista_resultante = notas_aprovadas(lista_notas_alunos)

print(f"Notas aprovadas")
print(lista_resultante)
