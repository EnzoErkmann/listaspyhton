class Elemento:
    def __init__(self, key, dado):
        self._key = key
        self._dado = dado

    def __str__(self):
        return f"({self._key}, {self._dado})"


class Pilha:
    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if self.esta_vazia():
            raise Exception("Pilha vazia")
        return self.itens.pop()

    def esta_vazia(self):
        return len(self.itens) == 0

    def topo(self):
        if self.esta_vazia():
            raise Exception("Pilha vazia")
        return self.itens[-1]

    def __str__(self):
        return "Pilha: " + " | ".join(str(e) for e in reversed(self.itens))


def remover_por_chave(pilha, chave):
    aux = Pilha()

    # Tira os elementos e guarda na aux, exceto o que tem a chave a ser removida
    while not pilha.esta_vazia():
        elemento = pilha.pop()
        if elemento._key != chave:
            aux.push(elemento)
        else:
            print(f"Elemento removido: {elemento}")

    # Restaura a pilha original (sem o elemento com chave c)
    while not aux.esta_vazia():
        pilha.push(aux.pop())

# Criando a pilha e colocando uns elementos
p = Pilha()
p.push(Elemento(1, "A"))
p.push(Elemento(2, "B"))
p.push(Elemento(3, "C"))
p.push(Elemento(4, "D"))

print("Antes:")
print(p)

# Remover elemento com chave 3
remover_por_chave(p, 3)

print("Depois:")
print(p)
