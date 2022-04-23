'''
FILA CIRCULAR
IMPLEMENTAÇÃO
'''

import numpy as np

class FilaCircular:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __fila_vazia(self):
        return self.numero_elementos == 0

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('Fila está cheia')
            return

        if self.final == self.capacidade -1:
            self.final = -1
        self.final += 1

        self.valores[self.final] = valor
        self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('Fila está vazia')
            return

        temp = self.valores[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade:
            self.inicio = 0

        self.numero_elementos -= 1
        return temp

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.inicio]

fila = FilaCircular(5)
#
#*+             ~> Inicio: 0 Final: -1
# _ _ _ _ _
print(fila.primeiro())
# +
# *             ~> Inicio: 0 Final: 0
# 1 _ _ _ _
fila.enfileirar(1)
print(fila.primeiro())
# * +           ~> Inicio: 0 Final: 1
# 1 2 _ _ _
fila.enfileirar(2)
fila.primeiro()
# *   +         ~> Inicio: 0 Final: 2
# 1 2 3 _ _
fila.enfileirar(3)
# *     +       ~> Inicio: 0 Final: 3
# 1 2 3 4 _
fila.enfileirar(4)
# *       +     ~> Inicio: 0 Final: 4
# 1 2 3 4 5
fila.enfileirar(5)
# Fila cheia    ~> Inicio: 0 Final: 4
fila.enfileirar(6)

#   *     +     ~> Inicio: 1 Final: 4
# _ 2 3 4 5
fila.desenfileirar()
#     *   +     ~> Inicio: 2 Final: 4
# _ _ 3 4 5
fila.desenfileirar()
print(fila.primeiro())

# +   *         ~> Inicio: 2 Final: 0 (-1 += 1)
# 6 _ 3 4 5
fila.enfileirar(6)
#   + *         ~> Inicio: 2 Final: 1
# 6 7 3 4 5
fila.enfileirar(7)
print(fila.primeiro())
print(fila.valores) # .valores deve ser privado -> __valores
print(fila.inicio, fila.final)
print(fila.valores[fila.inicio], fila.valores[fila.final])

