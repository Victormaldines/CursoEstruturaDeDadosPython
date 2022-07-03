'''
ÁRVORE BINÁRIA DE BUSCA - EXCLUSÃO
O NÓ A SER APAGADO TEM DOIS FILHOS
    * O nó a ser apagado deve ser substituído por seu sucessor em ordem
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
        if self.raiz == None:
            print('Árvore está vazia')
            return

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
            self.pre_ordem(no.esquerda)
            print(no.valor)
            self.pre_ordem(no.direita)

    def pos_ordem(self, no):
        if no != None:
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)
            print(no.valor)

    def exclui(self, valor):
        if self.raiz == None:
            print('A árvore está vazia')
            return

        atual = self.raiz
        pai = self.raiz
        e_esquerda = True

        while valor != atual.valor:
            pai = atual
            if valor < atual.valor:
                atual = atual.esquerda
                e_esquerda = True
            else:
                atual = atual.direita
                e_esquerda = False
            if atual == None:
                return False

         # Nó a ser excluído é um nó-folha
        if atual.esquerda == None and atual.direita == None:
            if e_esquerda:
                self.ligacoes.remove(str(pai.valor) + '->' + str(atual.valor))
                pai.esquerda = None
            else:
                self.ligacoes.remove(str(pai.valor) + '->' + str(atual.valor))
                pai.direita = None
        # Se houver apenas um filho à direita
        elif atual.esquerda == None:
            if e_esquerda:
                pai.esquerda = atual.direita
            else:
                pai.direita = atual.direita
        elif atual.direita == None:
            if e_esquerda:
                pai.esquerda = atual.esquerda
            else:
                pai.direita = atual.esquerda

        # Nó possui dois filhos
        else:
            sucessor = self.get_sucessor(atual)

            if sucessor == self.raiz:
                self.raiz = sucessor
            elif e_esquerda == True:
                pai.esquerda = sucessor
            else:
                pai.direita = sucessor

            sucessor.esquerda = atual.esquerda

        return True

    def get_sucessor(self, no):
        pai_sucessor = no
        sucessor = no
        atual = no.direita

        while atual != None:
            pai_sucessor = sucessor
            sucessor = atual
            atual = atual.esquerda
        if sucessor != no.direita:
             pai_sucessor.esquerda = sucessor.direita
             sucessor.direita = no.direita
        return sucessor

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

arvore.exclui(72)
print('a')
