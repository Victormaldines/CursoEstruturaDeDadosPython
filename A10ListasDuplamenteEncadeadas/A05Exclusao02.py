class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

    def mostra_no(self):
        print(self.valor)

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __lista_vazia(self):
        return self.primeiro == None

    def insere_inicio(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.ultimo = novo
        else:
            self.primeiro.anterior = novo
        novo.proximo = self.primeiro
        self.primeiro = novo

    def insere_final(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
        novo.anterior = self.ultimo
        self.ultimo = novo

    def exclui_inicio(self):
        if self.__lista_vazia():
            print('Lista está vazia')
            return

        temp = self.primeiro

        if self.primeiro.proximo == None:
            self.ultimo = None
        else:
            self.primeiro.proximo.anterior = None
        self.primeiro = self.primeiro.proximo
        return temp

    def exclui_final(self):
        if self.__lista_vazia():
            print('Lista está vazia')
            return

        temp = self.ultimo

        if self.primeiro.proximo == None:
            self.primeiro = None
        else:
            self.ultimo.anterior.proximo = None
        self.ultimo = self.ultimo.anterior
        return temp

    def exclui_posicao(self, valor):
        if self.__lista_vazia():
            print('Lista está vazia')
            return

        atual = self.primeiro
        while atual.valor != valor:
            atual = atual.proximo
            if atual == None:
                return None

        if atual == self.primeiro:
            self.primeiro = atual.proximo
        else:
            atual.anterior.proximo = atual.proximo

        if atual == self.ultimo:
            self.ultimo = atual.anterior
        else:
            atual.proximo.anterior = atual.anterior
        return atual

    def mostra_frente(self):
        if self.__lista_vazia():
            print('Lista está vazia')
            return

        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo

    def mostra_tras(self):
        if self.__lista_vazia():
            print('Lista está vazia')
            return

        atual = self.ultimo
        while atual != None:
            atual.mostra_no()
            atual = atual.anterior

lista = ListaDuplamenteEncadeada()
lista.insere_inicio(1)
lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)
lista.mostra_frente()
print()
lista.exclui_posicao(3)
lista.mostra_frente()
lista.exclui_posicao(5)
lista.exclui_posicao(1)
print(lista.primeiro, lista.ultimo)
lista.mostra_frente()

