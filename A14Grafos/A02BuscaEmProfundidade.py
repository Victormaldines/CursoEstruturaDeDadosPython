'''
GRAFO - BUSCA EM PROFUNDIDADE
* REGRA 1
    * Visite um nó adjacente não visitado, marque-o e coloque-o na pilha

* REGRA 2
    * Se não puder seguir a Regra 1, retire o nó da pilha

* REGRA 3
    * Se não puder seguir a Regra 1 ou Regra 2, terminou

* Analogia: labirinto utilizando uma corda
'''

import numpy as np

class Vertice:
    def __init__(self, rotulo):
        self.rotulo = rotulo
        self.visitado = False
        self.adjacentes = []

    def adiciona_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)

    def mostra_adjacentes(self):
        for i in self.adjacentes:
            print(i.vertice.rotulo, i.custo)

class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo

class Grafo:
    arad = Vertice('Arad')
    zerind = Vertice('Zerind')
    oradea = Vertice('Oradea')
    sibiu = Vertice('Sibiu')
    timisoara = Vertice('Timisoara')
    lugoj = Vertice('Lugoj')
    mehadia = Vertice('Mehadia')
    dobreta = Vertice('Dobreta')
    craiova = Vertice('Craiova')
    rimnicu = Vertice('Rimnicu')
    fagaras = Vertice('Fagaras')
    pitesti = Vertice('Pitesti')
    bucharest = Vertice('Bucharest')
    giurgiu = Vertice('Giurgiu')

    arad.adiciona_adjacente(Adjacente(zerind, 75))
    arad.adiciona_adjacente(Adjacente(sibiu, 140))
    arad.adiciona_adjacente(Adjacente(timisoara, 118))

    zerind.adiciona_adjacente(Adjacente(arad, 75))
    zerind.adiciona_adjacente(Adjacente(oradea, 71))

    oradea.adiciona_adjacente(Adjacente(zerind, 71))
    oradea.adiciona_adjacente(Adjacente(sibiu, 151))

    sibiu.adiciona_adjacente(Adjacente(arad, 140))
    sibiu.adiciona_adjacente(Adjacente(oradea, 151))
    sibiu.adiciona_adjacente(Adjacente(rimnicu, 80))
    sibiu.adiciona_adjacente(Adjacente(fagaras, 99))

    timisoara.adiciona_adjacente(Adjacente(arad, 118))
    timisoara.adiciona_adjacente(Adjacente(lugoj, 111))

    lugoj.adiciona_adjacente(Adjacente(timisoara, 111))
    lugoj.adiciona_adjacente(Adjacente(mehadia, 70))

    mehadia.adiciona_adjacente(Adjacente(lugoj, 70))
    mehadia.adiciona_adjacente(Adjacente(dobreta, 75))

    dobreta.adiciona_adjacente(Adjacente(mehadia, 75))
    dobreta.adiciona_adjacente(Adjacente(craiova, 120))

    craiova.adiciona_adjacente(Adjacente(dobreta, 120))
    craiova.adiciona_adjacente(Adjacente(rimnicu, 146))
    craiova.adiciona_adjacente(Adjacente(pitesti, 138))

    pitesti.adiciona_adjacente(Adjacente(craiova, 138))
    pitesti.adiciona_adjacente(Adjacente(rimnicu, 97))
    pitesti.adiciona_adjacente(Adjacente(bucharest, 101))

    fagaras.adiciona_adjacente(Adjacente(sibiu, 99))
    fagaras.adiciona_adjacente(Adjacente(bucharest, 211))

    rimnicu.adiciona_adjacente(Adjacente(sibiu, 80))
    rimnicu.adiciona_adjacente(Adjacente(craiova, 146))
    rimnicu.adiciona_adjacente(Adjacente(pitesti, 101))

    bucharest.adiciona_adjacente(Adjacente(fagaras, 211))
    bucharest.adiciona_adjacente(Adjacente(pitesti, 101))
    bucharest.adiciona_adjacente(Adjacente(giurgiu, 90))

class Pilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        # Mudança no tipo do Array
        self.__valores = np.empty(self.__capacidade, dtype=object)

    def __pilha_vazia(self):
        if self.__topo == -1:
            return True
        return False

    def __pilha_cheia(self):
        if self.__topo == self.__capacidade -1:
            return True
        return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
           print('Pilha está cheia')
           return

        self.__topo += 1
        self.__valores[self.__topo] = valor

    def desempilhar(self):
        if self.__pilha_vazia():
            print('Pilha está vazia')
            return None

        temp = self.__valores[self.__topo]
        self.__topo -= 1
        return temp

    def ver_topo(self):
        if self.__topo != -1:
            return self.__valores[self.__topo]
        return -1

grafo = Grafo()

class BuscaProfundidade:
    def __init__(self, inicio):
        self.inicio = inicio # vertice
        self.inicio.visitado = True
        self.pilha = Pilha(20)
        self.pilha.empilhar(inicio)

    def buscar(self):
        topo = self.pilha.ver_topo()
        print('Topo: {}'.format(topo.rotulo))
        for adjacente in topo.adjacentes:
            print('Topo é {}. {} já foi visitada? {}'.format(topo.rotulo, adjacente.vertice.rotulo, adjacente.vertice.visitado))
            if adjacente.vertice.visitado == False:
                adjacente.vertice.visitado = True
                self.pilha.empilhar(adjacente.vertice)
                print('Empilhou {}'.format(adjacente.vertice.rotulo))
                self.buscar()
        print('Desempilhou {}'.format(self.pilha.desempilhar().rotulo))
        print()

busca_profundidade = BuscaProfundidade(grafo.arad)
busca_profundidade.buscar()
