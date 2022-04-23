class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self):
        print(self.valor)

class ListaEncadeadaExtremidadeDupla:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __lista_vazia(self):
        return self.primeiro == None

    def insere_inicio(self, valor):
        novo = No(valor)
        # Se lista estiver vazia
        if self.__lista_vazia():
            self.ultimo = novo
        novo.proximo = self.primeiro
        self.primeiro = novo

    def insere_final(self, valor):
        novo = No(valor)
        # Se lista estiver vazia
        if self.__lista_vazia():
            self.primeiro = novo
            self.ultimo = novo
            return
        self.ultimo.proximo = novo
        self.ultimo = novo

    def exclui_inicio(self):
        if self.__lista_vazia():
            print('Lista está vazia')
            return

        temp = self.primeiro

        # Somente há um elemento na lista
        if self.primeiro.proximo == None:
            self.ultimo = None

        self.primeiro = self.primeiro.proximo
        return temp


    def mostra(self):
        if self.__lista_vazia():
            print('Lista está vazia')
            return

        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo

lista = ListaEncadeadaExtremidadeDupla()
lista.insere_inicio(1)
lista.insere_final(3)
lista.mostra()
print()
lista.exclui_inicio()
lista.mostra()
lista.exclui_inicio()
lista.exclui_inicio()
lista.mostra()
