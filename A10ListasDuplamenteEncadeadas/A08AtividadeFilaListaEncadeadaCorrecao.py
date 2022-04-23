class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self):
        print(self.valor)

class ListaEncadadeadaExtremidadeDupla:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __lista_vazia(self):
        return self.primeiro == None

    def insere_final(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
        self.ultimo = novo

    def excluir_inicio(self):
        if self.__lista_vazia():
            print('Lista está vazia')
            return
        temp = self.primeiro
        if self.primeiro.proximo == None:
            self.ultimo = None
        self.primeiro = self.primeiro.proximo
        return temp

class FilaListaEncadeada:
    def __init__(self):
        self.lista = ListaEncadadeadaExtremidadeDupla()

    def fila_vazia(self):
         return self.lista.__lista_vazia()

    def enfileirar(self, valor):
        self.lista.insere_final(valor)

    def desenfileirar(self):
        self.lista.excluir_inicio()

    def ver_inicio(self):
        if self.lista.primeiro == None:
            return -1
        return self.lista.primeiro.valor

fila = FilaListaEncadeada()
# 20
fila.enfileirar(20)
# 40 20
fila.enfileirar(40)
print(fila.ver_inicio())
# 60 40 20
fila.enfileirar(60)
# 80 60 40 20
fila.enfileirar(80)
print(fila.ver_inicio())
# 80 60 40
fila.desenfileirar()
print(fila.ver_inicio())
# 80 60
fila.desenfileirar()
# 80
fila.desenfileirar()
#
fila.desenfileirar()
print(fila.ver_inicio())