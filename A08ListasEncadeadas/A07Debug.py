class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self):
        print(self.valor)

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def __lista_vazia(self):
        return self.primeiro == None

    def insere_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostra(self):
        if self.__lista_vazia():
            print('Lista está vazia')
            return

        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo

    def pesquisa(self, valor):
        if self.__lista_vazia():
            print('Lista está vazia')
            return

        atual = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            atual = atual.proximo
        return atual

    def exclui_inicio(self):
        if self.__lista_vazia():
            print('Lista está vazia')
            return

        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp

    def exclui_posicao(self,valor):
        if self.__lista_vazia():
            print('A lista está vazia')
            return

        atual = self.primeiro
        anterior = self.primeiro

        while atual.valor != valor:
            if atual.proximo == None:
                return None
            anterior = atual
            atual = atual.proximo

        if atual == self.primeiro:
            self.primeiro = self.primeiro.proximo
        else:
            anterior.proximo = atual.proximo

        return atual

lista = ListaEncadeada()
lista.insere_inicio(1)
lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)
pesquisa = lista.pesquisa(3)
lista.exclui_inicio()
lista.exclui_posicao(4)
lista.exclui_posicao(2)

