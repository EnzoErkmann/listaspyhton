def medialista(x):
    contador = 0
    i = 0
    for i in x:
        contador += i
    media = contador / len(x)
    return media

fila = [3, 4, 6, 7, 1, 3]
print(f"\nA média dos elementos da lista é: {medialista(fila)}\n")