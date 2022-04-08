# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 22:05:00 2022

@author: vitu
ESTRUTURAS DE REPETIÇÃO
"""

print(1)
print(2)
print(3)
print(4)
print(5)
print('\n')

# FOR

                            # O loop não inclui o upper bound (limite superior)
for numero in range(1, 6): # Realiza a repetição do laço no range 1 até o range 6 (1, 2, 3, 4, 5)
    print(numero)
print('\n')

for numero in range(5, 0, -1): # Realiza a repetiçaõ do laço no range 5 até o range 0 com o step -1 (5, 4, 3, 2, 1)
    print(numero)
print('\n')

# 1 + 2 + 3 + 4 + 5
soma = 0
for numero in range(1, 6): # Realiza a repetição do laço no range 1 até o 6 (1, 2, 3, 4, 5)
    soma = soma + numero
    #print(soma)
print(soma, '\n')

palavra = 'sorvete'
for letra in palavra: # Realiza a repetição do laço para cada caractere dentro da string <palavra='sorvete'>
    print(letra)
    if letra == 'v':
        print('Achou a letra v')
print('\n')

# FOR ANINHADO
for i in range(0, 5): # Realiza a repetição do laço no range 0 até o 5 (1, 2, 3, 4)
    print(i)
    print('---')
    for j in range(0, 3): # Realiza a repetição do laço no range 0 até o 3 (0, 1, 2)
        print(j)
    print('\n')