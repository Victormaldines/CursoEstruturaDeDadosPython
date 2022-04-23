"""
VETOR ORDENADO
INSERÇÃO
"""

import numpy as np

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultima_posicao == -1:
            print('Vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print('Indice:', i, 'valor:', self.valores[i])
    # O(n)
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade -1:
            print('Capacidade máxima atingida')
            return

        posicao = 0
        for i in range(self.ultima_posicao+1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x+1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

vetor = VetorOrdenado(10)
vetor.imprime()
vetor.insere(6)
vetor.insere(4)
vetor.insere(3)
vetor.insere(5)
vetor.insere(1)
vetor.insere(8)
vetor.imprime()




















''' meu deus
    def insere(self, valor):
        if self.ultima_posicao == -1:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor
        else:
            if self.ultima_posicao == self.capacidade - 1:
                print('Vetor está cheio')
            else:
                index = 0
                while valor > self.valores[index] and index < self.ultima_posicao+1:
                    index+=1

                for i in range(self.ultima_posicao+1, index, -1):
                    self.valores[i] = self.valores[i-1]
                self.valores[index] = valor
                self.ultima_posicao += 1
                
                
vetor = VetorOrdenado(10)
vetor.insere(42)
vetor.insere(11)
vetor.insere(81)
vetor.insere(66)
vetor.insere(81)
vetor.insere(51)
vetor.insere(11)
vetor.insere(89)
vetor.imprime()

'''
