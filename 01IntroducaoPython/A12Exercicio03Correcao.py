# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 17:44:25 2022

@author: vitu
"""

# 3. MATRIZ

import numpy as np
matriz = np.array([[3, 4, 1], [3, 1, 5]])

soma = 0
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        soma += matriz[i][j]
print('Soma:', soma)