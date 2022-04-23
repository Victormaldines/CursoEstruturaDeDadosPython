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
    
    def pesquisa(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return -1
    
    # O(n)
    def excluir(self, valor):
        posicao = self.pesquisa(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i+1]
            self.ultima_posicao -= 1
        
                
vetor = VetorNaoOrdenado(10)

vetor.insere(3)
vetor.insere(2)
vetor.insere(4)
vetor.insere(5)
vetor.insere(6)
vetor.insere(1)
vetor.imprime()

vetor.pesquisa(5)
vetor.pesquisa(9)

vetor.excluir(5)
