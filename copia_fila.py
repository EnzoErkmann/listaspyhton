def copiafila(x1):
    x2 = [] #lembrar de daclarar outra fila
    for i in x1:
        x2.append(i)
    return x2

fila = [3, 4, 6, 7, 1, 3] #dá pra fazercom append também mas né
print(f"\nA fila original é: {fila}")
print(f"\nA copia da fila é: {copiafila(fila)}\n")