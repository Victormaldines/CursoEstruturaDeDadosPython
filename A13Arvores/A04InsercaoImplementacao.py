class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def mostraNo(self):
        print(self.valor)

class ArvoreBuscaBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        novo = No(valor)
        # Se a árvore estiver vazia:
        if self.raiz == None:
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                pai = atual
                # Esquerda
                if valor < atual.valor:
                    atual = pai.esquerda
                    if atual == None:
                        pai.esquerda = novo
                        return
                # Direita
                else:
                    atual = pai.direita
                    if atual == None:
                        pai.direita = novo
                        return

# Inserção e visualização
arvore = ArvoreBuscaBinaria()
arvore.inserir(53)
arvore.inserir(30)
arvore.inserir(14)
arvore.inserir(39)
arvore.inserir(9)
arvore.inserir(23)
arvore.inserir(34)
arvore.inserir(49)
arvore.inserir(72)
arvore.inserir(61)
arvore.inserir(84)
arvore.inserir(79)
print(arvore.raiz.valor)
print(arvore.raiz.esquerda.esquerda.esquerda.valor)