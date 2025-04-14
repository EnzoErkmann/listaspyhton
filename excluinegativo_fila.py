def excluinega(x):
    i = 0
    while i < len(x):
        if x[i] < 0:
            x.pop(i)
        else:
            i += 1 #ele não altera i quando remove daí não faz bagunça diferente do contapar
    return x 

fila = [] # ou só faz fila = [5, -1, 453, etc] e sem os appends
fila.append(5)
fila.append(-1)
fila.append(-53)
fila.append(4)
fila.append(53)
fila.append(0)
print(f"\nA fila sem os números negativos é: {excluinega(fila)}\n")