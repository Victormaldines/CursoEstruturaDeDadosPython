import numpy as np

class FilaPrioridade:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def fila_vazia(self):
        return self.numero_elementos == 0

    def fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def enfileirar(self, valor):
        if self.fila_cheia():
            print('Fila está cheia')
            return

        if self.numero_elementos == 0:
            self.valores[self.numero_elementos] = valor
            self.numero_elementos += 1
        else:
            x = self.numero_elementos -1
            while x >= 0:
                if valor >= self.valores[x]:
                    self.valores[x+1] = self.valores[x]
                else:
                    break
                x -= 1
            self.valores[x + 1] = valor
            self.numero_elementos += 1

    def desenfileirar(self):
        if self.fila_vazia():
            print('Fila está vazia')
            return

        temp = self.valores[self.numero_elementos -1]
        self.numero_elementos -= 1
        return temp

    def primeiro(self):
        if self.fila_vazia():
            return -1
        return self.valores[self.numero_elementos-1]

fila = FilaPrioridade(5)
print(fila.primeiro())
# *
# 30 _ _ _ _
fila.enfileirar(30)
print(fila.primeiro())
#    *
# 50 30 _ _ _
fila.enfileirar(50)
print(fila.primeiro())
#       *
# 50 30 10
fila.enfileirar(10)
print(fila.primeiro())
print(fila.valores)

#          *
# 50 40 30 10 _
fila.enfileirar(40)
print(fila.valores)

fila.enfileirar(20)

#             *
# 50 40 30 20 10
print(fila.valores)

fila.enfileirar(2)
fila.desenfileirar()
print(fila.primeiro())
fila.desenfileirar()
print(fila.primeiro())
fila.desenfileirar()
print(fila.primeiro())
#       *
# 50 40 5 _ _
fila.enfileirar(5)
print(fila.primeiro())
print(fila.valores)