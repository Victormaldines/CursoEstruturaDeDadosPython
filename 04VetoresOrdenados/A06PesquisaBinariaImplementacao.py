import numpy as np

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('Vetor está vazio')
        else:
            for i in range(self.ultima_posicao+1):
                print(self.valores[i])

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Vetor já está cheio')
            return

        # Encontra a posição na qual o indice será inserido
        posicao = 0
        for i in range(self.ultima_posicao+1):
            posicao = i
            if valor < self.valores[i]:
                break
            if i == self.ultima_posicao:
                posicao += 1

        # Remaneja os elementos para inserção do novo elemento
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x+1] = self.valores[x]
            x -= 1
        # Insere o novo elemento e seta o novo tamanho útil do vetor
        self.valores[posicao] = valor
        self.ultima_posicao += 1

    def pesquisa_linear(self, valor):
        for i in range(self.ultima_posicao+1):
            if valor == self.valores[i]:
                return i
            if valor < self.valores[i] or i == self.ultima_posicao:
                return -1

    # O(log n)
    def pesquisa_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao

        while True:
            posicao_atual = int((limite_inferior + limite_superior) / 2)
            # Se achou na primeira tentativa
            if self.valores[posicao_atual] == valor:
                return posicao_atual
            # Se não achou em nenhuma posição
            elif limite_inferior > limite_superior:
                return -1

            # Divide os limites
            else:
                # Limite inferior
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1
                else:
                    limite_superior = posicao_atual - 1

    # O(n)
    def excluir(self, valor):
        posicao = self.pesquisaLinear(valor)
        if posicao == -1:
            return -1
        for i in range(posicao, self.ultima_posicao):
            self.valores[i] = self.valores[i+1]
        self.ultima_posicao -= 1

vetor = VetorOrdenado(10)
vetor.insere(8)
vetor.insere(9)
vetor.insere(4)
vetor.insere(1)
vetor.insere(5)
vetor.insere(7)
vetor.insere(11)
vetor.insere(13)
vetor.insere(2)

vetor.pesquisa_binaria(7)
vetor.pesquisa_binaria(5)
vetor.pesquisa_binaria(13)
vetor.pesquisa_binaria(20)