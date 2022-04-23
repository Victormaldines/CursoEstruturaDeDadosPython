'''
LISTA ENCADEADA SIMPLES
INSERE NO INÍCIO E MOSTRA
'''

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

    def mostrar(self):
        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo

## INSERE NO INICIO ##
lista = ListaEncadeada()

lista.insere_inicio(1)
print(lista.primeiro)
lista.insere_inicio(2)
print(lista.primeiro)
print(lista.primeiro)
lista.mostrar()
print(lista.primeiro.proximo)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(4)
lista.mostrar()
print(lista.primeiro)
lista.primeiro.mostra_no()
print(lista.primeiro.proximo) # 4
print(lista.primeiro.proximo.proximo) # 3
print(lista.primeiro.proximo.proximo.proximo) # 2
print(lista.primeiro.proximo.proximo.proximo.proximo) # 1
print(lista.primeiro.proximo.proximo.proximo.proximo.proximo) # None ~> Fim
