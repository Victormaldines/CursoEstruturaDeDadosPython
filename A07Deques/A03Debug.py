import numpy as np

class Deque:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = -1
        self.final = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __deque_cheio(self):
        return (self.inicio == 0 and self.final == self.capacidade -1) or (self.inicio == self.final + 1)

    def __deque_vazio(self):
        return self.inicio == -1

    def insere_inicio(self, valor):
        if self.__deque_cheio():
            print('Deque está cheio')
            return

        # SE DEQUE ESTIVER VAZIO
        if self.inicio == -1:
            self.inicio = 0
            self.final = 0
        # SE INICIO DO DEQUE ESTIVER NO COMEÇO ~> x _ _ _ _
        elif self.inicio == 0:
            self.inicio = self.capacidade -1
        else:
            self.inicio -= 1

        self.valores[self.inicio] = valor

    def insere_final(self, valor):
        if self.__deque_cheio():
            print('Deque está cheio')
            return

        # SE DEQUE ESTIVER VAZIO
        if self.inicio == -1:
            self.inicio = 0
            self.final = 0
        # SE FINA DO DEQUE ESTIVER NO FINAL ~> _ _ _ _ x
        elif self.final == self.capacidade -1:
            self.final = 0
        else:
            self.final += 1

        self.valores[self.final] = valor

    def excluir_inicio(self):
        if self.__deque_vazio():
            print('Deque está vazio')
            return

        # SE EXISTIR APENAS UM ELEMENTO NO DEQUE
        if self.inicio == self.final:
            self.inicio = -1
            self.final = -1
        # SE INICIO ESTIVER NO FINAL
        elif self.inicio == self.capacidade -1:
            self.inicio = 0
        else:
            self.inicio += 1

    def excluir_final(self):
        if self.__deque_vazio():
            print('Deque está vazio')
            return

        # SE EXISTIR APENAS UM ELEMENTO
        if self.inicio == self.final:
            self.inicio = -1
            self.final = -1
        # SE FINAL ESTIVER NO COMEÇO
        elif self.final == 0:
            self.final = self.capacidade -1
        else:
            self.final -= 1

    def get_inicio(self):
        if self.__deque_vazio():
            print('Deque está vazio')
            return -1
        return self.valores[self.inicio]

    def get_final(self):
        if self.__deque_vazio() or self.final < 0:
            print('Deque está vazio')
            return -1
        return self.valores[self.valores]

deque = Deque(5)
deque.insere_final(5)
deque.insere_final(10)
deque.insere_inicio(3)
deque.insere_inicio(2)
deque.insere_final(11)

deque.insere_inicio(43)

deque.excluir_inicio()
deque.excluir_final()
