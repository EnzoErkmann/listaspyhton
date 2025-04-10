class Pilha:
    def __init__(self):
        self.itens = []

    def push(self, valor):
        self.itens.append(valor)

    def pop(self):
        if not self.esta_vazia():
            return self.itens.pop()
        return None

    def esta_vazia(self):
        return len(self.itens) == 0

    def __str__(self):
        return str(self.itens)
    
def inverter_pilha(pilha):
    pilha_invertida = Pilha() #cria mais uma pilha na classe pilha, fez isso pra ter mais uma
    while not pilha.esta_vazia():
        pilha_invertida.push(pilha.pop())
    return pilha_invertida

g = Pilha()
g.push(3)
g.push(43)
g.push(323)

print("\ntoma normalzinha tlgd: ",g)

reversi = inverter_pilha(g)
print("\nSegura o reversi: ",reversi)