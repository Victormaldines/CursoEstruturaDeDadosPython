# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 17:04:51 2022

@author: vitu

MATRIZES
"""

import numpy as np

matriz = np.array([[2, 3, 1],
                   [5, 5, 7]])

print(matriz)
print()

print(matriz.shape)
print()

print(matriz[0])
print()

print(matriz[1])
print()

print(matriz[0][2])
print(matriz[1][0])
print()

for i in range(matriz.shape[0]):
    print(matriz[i])
    for j in range(matriz.shape[1]):
        print(matriz[i][j])
