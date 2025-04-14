def coisa_pilha(x): #define função como pilha e bota variavel e só declara como pilha uma variavel fora da função
    maior = x[0] # versão com classes no chatgpt
    menor = x[0]
    sum = 0

    for i in x:
        if i > maior:
            maior = i
        if i < menor:
            menor = i
        sum += i
    media = i / len(x)
    
    print(f"maior: {maior}")
    print(f"menor: {menor}")
    print(f"Média: {media}")

pilha = []
pilha.append(5)
pilha.append(3)
pilha.append(5)
pilha.append(7)
pilha.append(32332)

coisa_pilha(pilha)