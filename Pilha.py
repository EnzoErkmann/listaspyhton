class Pilha:
    def __init__(self):
        self.itens = []

    def push(self, valor):
        self.itens.append(valor)

    def pop(self):
        if not self.vazia():
            return self.itens.pop()  # remove e retorna o topo
        else:
            return None  # ou lançar uma exceção

    def topo(self):
        if not self.vazia():
            return self.itens[-1]
        else:
            return None

    def vazia(self):
        return len(self.itens) == 0

    def mostrar(self):
        print(self.itens)

pilha = Pilha()

pilha.push(5)
pilha.push(3)
print(pilha.pop())  # saída: 3
pilha.push(2)
pilha.push(8)
print(pilha.pop())   # saída: 8
print(pilha.pop())   # saída: 2
pilha.push(9)
pilha.mostrar()      # saída: [5, 9]