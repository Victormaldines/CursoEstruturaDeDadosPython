'''
ÁRVORE BINÁRIA DE BUSCA - EXCLUSÃO
O NÓ A SER APAGADO TEM APENAS UM FILHO

* O Nó tem apenas duas conexões: com seu pai e com seu único filho
* Deseja-se "cortar" o nó dessa sequência conectando o pai dele diretamente ao filho dele

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
        return valor

    # raiz, esquerda, direita
    def pre_ordem(self, no):
        if no != None:
            print(no.valor)
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)

    # esquerda, raiz, direita
    def em_ordem(self, no):
        if no != None:
            self.em_ordem(no.esquerda)
            print(no.valor)
            self.em_ordem(no.direita)

    # esquerda, direita, raiz
    def pos_ordem(self, no):
        if no != None:
            self.pos_ordem(no.esquerda)
            self.pos_ordem(no.direita)
            print(no.valor)

    def excluir(self, valor):
        if self.raiz == None:
            print('Árvore está vazia')
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

        # Verifica se o nó (atual) é uma folha
        if atual.esquerda == None and atual.direita == None:
            if atual == self.raiz:
                self.raiz = None
            elif e_esquerda:
                pai.esquerda = None
            else:
                pai.direita = None

        # nó com filho único
        # O nó a ser apagado não possui filho na direita (nó a ser APAGADO é o ESQUERDO)
        elif atual.direita == None:
            if atual == self.raiz:
               self.raiz = atual.esquerda
            elif e_esquerda:
                pai.esquerda = atual.esquerda
            else:
                pai.direita = atual.esquerda
        # O nó a ser apagado não possui filho na esquerda (nó a ser APAGADO é o DIREITO)
        elif atual.esquerda == None:
            if atual == self.raiz:
                self.raiz = atual.direita
            elif e_esquerda:
                pai.esquerda = atual.direita
            else:
                pai.direita = atual.direita

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

arvore.excluir(84)
arvore.excluir(9)
arvore.excluir(14)
print('a')