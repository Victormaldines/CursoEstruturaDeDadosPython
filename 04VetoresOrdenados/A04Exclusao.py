import numpy as np

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao+1):
                print('Indice', i, 'Valor', self.valores[i])

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade -1:
            print('Capacidade máxima atingida')
            return

        posicao = 0
        for i in range(self.ultima_posicao+1):
            posicao = i
            if valor < self.valores[i]:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x+1] = self.valores[x]
            x -= 1
        self.valores[posicao] = valor
        self.ultima_posicao += 1

    # O(n)
    def pesquisa(self, valor):
        for i in range(self.ultima_posicao+1):
            if valor < self.valores[i]:
                return -1
            if valor == self.valores[i]:
                return i
            if i == self.ultima_posicao:
                return -1
    # O(n)
    def excluir(self, valor):
        posicao = self.pesquisa(valor)
        if posicao == -1:
            return -1
        for i in range(posicao, self.ultima_posicao):
            self.valores[i] = self.valores[i+1]
        self.ultima_posicao -= 1

vetor = VetorOrdenado(10)

vetor.insere(6)
vetor.insere(4)
vetor.insere(3)
vetor.insere(5)
vetor.insere(1)
vetor.insere(8)

vetor.pesquisa(3)
vetor.pesquisa(2)
vetor.pesquisa(9)

vetor.excluir(5)
vetor.excluir(9)
