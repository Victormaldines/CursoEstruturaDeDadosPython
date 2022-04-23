class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class PilhaListaEncadeada():
    def __init__(self):
        self.primeiro = None

    def __pilha_vazia(self):
        return self.primeiro == None

    def empilhar(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def desempilhar(self):
        if self.__pilha_vazia():
            print('Pilha está vazia')
            return

        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp

    def ver_topo(self):
        if self.__pilha_vazia():
            print('Pilha está vazia')
            return

        return self.primeiro.valor

pilha = PilhaListaEncadeada()
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(4)
print(pilha.ver_topo())
pilha.desempilhar()
pilha.desempilhar()
print(pilha.ver_topo())
