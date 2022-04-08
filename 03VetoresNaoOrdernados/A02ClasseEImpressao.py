"""
VETOR NÃO ORDENADO
CLASSE E IMPRESSÃO
"""

import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)
    
    # O(1), O(n) ~> O(n)
    def imprime(self):
        # O(1)
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        # O(n)
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, '-', self.valores[i])

vetor = VetorNaoOrdenado(5)
vetor.imprime()
