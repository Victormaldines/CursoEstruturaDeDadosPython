'''
ÁRVORE BINÁRIA - TRAVESSIA PÓS-ORDEM
* Recursivamente faz a travessia na subárvore esquerda, faz uma travessia recursiva na subárvore direita e por fim
visita a raiz
* Esquerda, direita, raiz
'''

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBuscaBinaria:
    def __init__(self):
        self.raiz = None
        self.ligacoes = []

    def insere(self, valor):
        novo = No(valor)
        if self.raiz == None:
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                pai = atual
                if valor < atual.valor:
                    atual = atual.esquerda
                    if atual == None:
                        pai.esquerda = novo
                        self.ligacoes.append(str(pai.valor) + '->' + str(valor))
                        return
                else:
                    atual = atual.direita
                    if atual == None:
                        pai.direita = novo
                        self.ligacoes.append(str(pai.valor) + '->' + str(valor))
                        return
    def buscar(self, valor):
        atual = self.raiz
        while valor != atual.valor:
            if valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita
            if atual == None:
                return None
        return atual

    def pre_ordem(self, no):
        if no != None:
            print(no.valor)
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)

    def em_ordem(self, no):
        if no != None:
            self.em_ordem(no.esquerda)
            print(no.valor)
            self.em_ordem(no.direita)

    def pos_ordem(self, no):
        if no != None:
            self.pos_ordem(no.esquerda)
            self.pos_ordem(no.direita)
            print(no.valor)

# Inserção e visualização
arvore = ArvoreBuscaBinaria()
arvore.insere(53)
arvore.insere(30)
arvore.insere(14)
arvore.insere(39)
arvore.insere(9)
arvore.insere(23)
arvore.insere(34)
arvore.insere(49)
arvore.insere(72)
arvore.insere(61)
arvore.insere(84)
arvore.insere(79)

# Travessia
arvore.pos_ordem(arvore.raiz)
print(arvore.ligacoes)


