# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 17:25:44 2022

@author: vitu
3. Dada a matriz abaixo, construa uma estrutura de repetição para percorrer
e somar todos os elementos da matriz:
    Matriz: [[3, 4, 1]
            [3, 1, 5]]
"""

import numpy as np

matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])

soma = 0
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        soma += matriz[i][j]        

print(soma)
