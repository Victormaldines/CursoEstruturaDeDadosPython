'''
ÁRVORE BINÁRIA DE BUSCA - EXCLUSÃO
* Inicia-se localizando o nó que deseja eliminar
* Cenários possíveis quando encontra-se o nó:
    - O nó a ser apagado é um nó-folha
    - O nó a ser apagado tem um filho
    - O nó a ser apagado tem dois filhos
'''

'''
O NÓ A SER APAGADO É UMA FOLHA
* A mais simples operação
* Altera o campo apropriado para o filho no nó pai para apontar para null/none, em vez do nó
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

    def pesquisa(self, valor):
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

    def excluir(self, valor):
        if self.raiz == None:
            print('A árvore está vazia')
            return False

        # Encontrar o nó
        atual = self.raiz
        pai = self.raiz
        e_esquerda = True # é esquerda / está na esquerda
        while valor != atual.valor:
            pai = atual
            # esquerda
            if valor < atual.valor:
                e_esquerda = True
                atual = atual.esquerda
            else:
                e_esquerda = False
                atual = atual.direita
            if atual == None:
                return False

        # O nó a ser apagado é uma folha
        if atual.esquerda == None and atual.direita == None:
            if atual == self.raiz:
                self.raiz = None
            elif e_esquerda:
                pai.esquerda = None
                self.ligacoes.remove(str(pai.valor) + '->' + str(valor))
            else:
                pai.direita = None
                self.ligacoes.remove(str(pai.valor) + '->' + str(valor))

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
arvore.em_ordem(arvore.raiz)
print(arvore.ligacoes)
arvore.excluir(9)
print(arvore.ligacoes)
arvore.excluir(61)
print(arvore.ligacoes)
arvore.excluir(79)
print(arvore.ligacoes)
arvore.excluir(84)
print(arvore.ligacoes)
arvore.excluir(23)
print(arvore.ligacoes)
print(arvore.excluir(100))
print(arvore.ligacoes)

