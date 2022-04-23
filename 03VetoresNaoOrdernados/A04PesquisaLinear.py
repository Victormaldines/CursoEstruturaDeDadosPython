"""
VETORES NÃO ORDENADOS
PESQUISA LINEAR
"""

import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)
    
    def imprime(self):
        if self.ultima_posicao == -1:
            print('Vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(self.valores[i])
    
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor
    
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao+1):
            if valor == self.valores[i]:
                return i
        return -1
    
    def pesquisar2(self, valor):
        valorTal = 0
        for i in range(self.ultima_posicao+1):
            if valor == self.valores[i]:
                valorTal = valor
        return valorTal
            

vetor = VetorNaoOrdenado(5)

vetor.imprime()
vetor.insere(2) #0
vetor.insere(3) #1
vetor.insere(5) #2
vetor.insere(8) #3
vetor.insere(1) #4
vetor.imprime()

print(vetor.pesquisar(8))
%timeit
            