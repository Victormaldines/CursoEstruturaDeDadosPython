'''
BUBBLE SORT
IMPLEMENTAÇÃO
'''

import numpy as np

def bubble_sort(vetor):
    n = len(vetor) # n ~> quantidade de elementos

    for i in range(n):
        for j in range(0, n - i - 1):
            if vetor[j] > vetor[j+1]:
                temp = vetor[j]
                vetor[j] = vetor[j+1]
                vetor[j+1] = temp

    return vetor

vetor = bubble_sort(np.array([15, 34, 8, 3]))
print(vetor)

vetorPiorCaso = bubble_sort(np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(vetorPiorCaso)


'''
class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimo = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def __vetor_cheio(self):
        return self.ultimo == self.capacidade -1

    def __vetor_vazio(self):
        return self.ultimo == -1

    def insere(self, valor):
        if self.__vetor_cheio():
            print('Vetor está cheio')
            return

        self.ultimo += 1
        self.valores[self.ultimo] = valor

    def bubble_sort(self):
        for i in range(self.ultimo+1):
            for j in range(0, self.ultimo+1 - i - 1):
                if self.valores[j] > self.valores[j+1]:
                    temp = self.valores[j]
                    self.valores[j] = self.valores[j+1]
                    self.valores[j+1] = temp

    def mostra(self):
        if self.__vetor_vazio():
            print('Vetor está vazio')
            return

        for i in range(self.ultimo+1):
            print(self.valores[i])

vetor = VetorNaoOrdenado(5)

vetor.insere(2)
vetor.insere(3)
vetor.insere(10)
vetor.insere(2)
vetor.insere(1)
vetor.mostra()
print()
vetor.bubble_sort()
vetor.mostra()

'''