# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 17:29:53 2022

@author: vitu
"""
# 1. LISTA

lista = []

for _ in range(1, 6):
    valor = int(input('Digite o valor: '))
    lista.append(valor)
    
soma = 0
for i in range(len(lista)):
    soma += lista[i]
print('Soma: ', soma)

import numpy as np
listaArray = np.array(lista)
print(listaArray.sum())

