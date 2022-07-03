'''
ARVORE BINÁRIA DE BUSCA - PESQUISA
Procurar nas subárvores da esquerda ou da direita
Vizualização online: https://visualgo.net/en/bst
Big-O: O(log n) para o caso medio e O(n) no pior caso
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

    def inserir(self, valor):
        novo = No(valor)
        if self.raiz == None:
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                pai = atual
                if atual.valor > valor:
                    atual = pai.esquerda
                    if atual == None:
                        pai.esquerda = novo
                        self.ligacoes.append(str(pai.valor) + '->' + str(novo.valor))
                        return
                else:
                    atual = pai.direita
                    if atual == None:
                        pai.direita = novo
                        self.ligacoes.append(str(pai.valor) + '->' + str(novo.valor))
                        return

    def pesquisar(self, valor):
        atual = self.raiz
        while atual.valor != valor:
            if valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita

            if atual == None:
                return None
        return atual

# Inserção e visualização
arvore = ArvoreBuscaBinaria()
arvore.inserir(53)
arvore.inserir(30)
arvore.inserir(14)
arvore.inserir(39)
arvore.inserir(9)
arvore.inserir(23)
arvore.inserir(34)
arvore.inserir(49)
arvore.inserir(72)
arvore.inserir(61)
arvore.inserir(84)
arvore.inserir(79)
arvore.inserir(89)

print(arvore.ligacoes)

arvore.pesquisar(39)
arvore.pesquisar(84)
arvore.pesquisar(100)

