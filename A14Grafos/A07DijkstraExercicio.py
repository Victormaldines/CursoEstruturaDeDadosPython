'''
ALGORITMO DE DIJKSTRA
Estrutura do grafo - matriz de adjacência

                                0 1 2 3 4
                                A B C D E
    A     D                0  A 0 0 1 0 0
     \  /                  1  B 0 0 1 0 0
      C  |        ==       2  C 1 1 0 1 1
     / \                   3  D 0 0 1 0 1
    B    E                 4  E 0 0 1 1 0

'''

import numpy as np
import sys

vertices = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}

vertices_inv = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}

arestas = np.zeros([len(vertices), len(vertices)], dtype=int)

arestas[vertices['A'], vertices['B']] = 2
arestas[vertices['A'], vertices['C']] = 1
arestas[vertices['B'], vertices['D']] = 1
arestas[vertices['C'], vertices['D']] = 3
arestas[vertices['C'], vertices['E']] = 4
arestas[vertices['D'], vertices['F']] = 2
arestas[vertices['E'], vertices['F']] = 2

class Dijkstra:
    def __init__(self, vertices, arestas, inicio):
        self.tamanho = len(vertices)
        self.vertices = vertices
        self.grafo = arestas
        self.inicio = inicio

    def mostra_solucao(self, distancias):
        print('Menores distâncias de {} até outras cidades'.format(self.vertices[self.inicio]))
        for vertice in range(self.tamanho):
            print(self.vertices[vertice], distancias[vertice])

    def distancia_minima(self, distancia, visitados):
        minimo = sys.maxsize
        for vertice in range(self.tamanho):
            if distancia[vertice] < minimo and visitados[vertice] == False:
                minimo = distancia[vertice]
                indice_minimo = vertice
        return indice_minimo

    def dijkstra(self):
        distancia = [sys.maxsize] * self.tamanho # [sys.maxsize, sys.maxsize..., sys.maxsize]
        distancia[self.inicio] = 0
        visitados = [False] * self.tamanho

        for _ in range(self.tamanho):
            indice_minimo = self.distancia_minima(distancia, visitados)
            visitados[indice_minimo] = True

            for vertice in range(self.tamanho):
                if self.grafo[indice_minimo][vertice] > 0 and visitados[vertice] == False \
                and distancia[vertice] > distancia[indice_minimo] + self.grafo[indice_minimo][vertice]:
                    distancia[vertice] = distancia[indice_minimo] + self.grafo[indice_minimo][vertice]

        self.mostra_solucao(distancia)

dijkstra = Dijkstra(vertices_inv, arestas, vertices['A'])
dijkstra.dijkstra()
print(arestas)

