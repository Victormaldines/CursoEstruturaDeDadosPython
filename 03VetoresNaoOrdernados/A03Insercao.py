"""
VETOR NÃO ORDENADO
INSERÇÃO
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
                print(i, '-', self.valores[i])
    
    # O(1),O(2) ~> O(1) constante
    def insere(self, valor):
        # O(1)
        if self.ultima_posicao == self.capacidade -1:
             print('Capacidade máxima atingida')
        # O(2)
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor
                
vetor = VetorNaoOrdenado(5)
vetor.imprime()
vetor.insere(2)
vetor.insere(3)
vetor.insere(5)
vetor.insere(8)
vetor.insere(1)
#vetor.insere(7)
vetor.imprime()
print(vetor.ultima_posicao)