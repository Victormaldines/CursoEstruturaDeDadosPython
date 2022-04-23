class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeadaExtremidadeDupla:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __lista_vazia(self):
        return self.primeiro == None

    def insere_inicio(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.ultimo = novo
        novo.proximo = self.primeiro
        self.primeiro = novo

    def exclui_final(self):
        if self.__lista_vazia():
            print('Lista está vazia')
            return

        if self.primeiro.proximo == None:
            self.primeiro = None
            self.ultimo = None
            return

        atual = self.primeiro
        anterior = self.primeiro
        while atual.proximo != None:
            anterior = atual
            atual = atual.proximo
        anterior.proximo = None
        self.ultimo = anterior
        return atual

    def ver_final(self):
        if self.__lista_vazia():
            print('Lista está vazia')
            return

        return self.ultimo.valor

class FilaListaEncadeada:
    def __init__(self):
        self.lista = ListaEncadeadaExtremidadeDupla()

    def enfileirar(self, valor):
        self.lista.insere_inicio(valor)

    def desenfileirar(self):
        return self.lista.exclui_final()

    def fila_vazia(self):
        return self.lista.__lista_vazia()

    def ver_inicio(self):
        return self.lista.ver_final()

fila = FilaListaEncadeada()
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
fila.desenfileirar()
fila.desenfileirar()
fila.desenfileirar()
print(fila.ver_inicio())
