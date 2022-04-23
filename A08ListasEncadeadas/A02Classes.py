'''
LISTA ENCADEADA SIMPLES
CLASSES
'''
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None # null, em C, Java...

    def mostra_no(self):
        print(self.valor)

class ListaEncadeada:

    def __init__(self):
        self.primeiro = None

no1 = No(1)
no1.mostra_no()

no2 = No(2)
no2.mostra_no()


