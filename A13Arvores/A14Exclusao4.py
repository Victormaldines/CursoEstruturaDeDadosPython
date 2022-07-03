'''
apenas reescrevendo o código para verificar compreensão
'''
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBuscaBinaria:
    def __init__(self):
        self.raiz = None

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
                        return
                else:
                    atual = atual.direita
                    if atual == None:
                        pai.direita = novo
                        return

    def pesquisa(self, valor):
        atual = self.raiz
        if valor != atual.valor:
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
            self.pre_ordme(no.direita)

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

    def exclui(self, valor):
        pai = self.raiz
        atual = self.raiz
        e_esquerda = True

        # Encontrar o nó a ser excluído
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

        # Se o nó a ser excluído (atual) for um nó-folha
        if atual.esquerda == None and atual.direita == None:
            if e_esquerda:
                pai.esquerda = None
            else:
                pai.direita = None

        # Se o nó a ser excluído (atual) tiver APENAS um filho à direita
        elif atual.esquerda == None:
            if e_esquerda:
                pai.esquerda = atual.direita
            else:
                pai.direita = atual.direita
        # Se o nó a ser excluído (atual) tiver APENAS um filho à esquerda
        elif atual.direita == None:
            if e_esquerda:
                pai.esquerda = atual.esquerda
            else:
                pai.direita = atual.esquerda

        else:
            sucessor = self.get_sucessor(atual)

            if sucessor == self.raiz:
                self.raiz = sucessor
            elif e_esquerda:
                pai.esquerda = sucessor
            else:
                pai.direita = sucessor

            sucessor.esquerda = atual.esquerda
        # Caso seja bem-sucedida a exclusão do nó
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


