'''
ÁRVORE BINÁRIA DE BUSCA
    * O filho à esquerda de um nó tem que ter uma chave menor que seu pai e o filho à direita de um nó tem que ter uma
    chave maior ou igual ao seu pai
'''

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def mostraNo(self):
        print(self.valor)

class ArvoreBinariaDeBusca:
    def __init__(self):
        self.raiz = None
