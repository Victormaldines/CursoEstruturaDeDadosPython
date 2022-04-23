class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self):
        print(self.valor)

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def insere_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def __lista_vazia(self):
        return self.primeiro == None

    def mostrar(self):
        if self.__lista_vazia():
            print('Lista está vazia')
            return

        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo

    def excluir_inicio(self):
        if self.__lista_vazia():
            print('A lista está vazia')
            return

        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp

### EXCLUIR DO INÍCIO
lista = ListaEncadeada()
lista.insere_inicio(1)
lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)
lista.mostrar()
print('\n')
lista.excluir_inicio()
lista.mostrar()
print('\n')
lista.excluir_inicio()
lista.excluir_inicio()
lista.mostrar()
print('\n')
lista.excluir_inicio()
lista.excluir_inicio()
lista.excluir_inicio()
