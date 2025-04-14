def contapar(x):
    contador = 0
    for i in x: # dá pra ser também for i in range(len(x)): acho que n faz diferença só não usa for i in x quando altera a fila
        if i % 2 == 0:
            contador += 1
    return contador

fila = [] 
fila.append(4)
fila.append(8)
fila.append(13)
fila.append(1)
fila.append(46)
print(f"\nQuantidade de números pares: {contapar(fila)}\n")