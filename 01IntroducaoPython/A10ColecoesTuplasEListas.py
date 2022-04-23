# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 14:24:29 2022

@author: vitu
# COLEÇÕES
- TUPLAS e LISTAS
"""

# TUPLAS - (entre parenteses)

tupla = ('Homo sapiens', 'Canis familiaris', 'Felis catus') # Variável declarada com o valor entre parênteses

print(tupla[0])
print(tupla.index('Canis familiaris')) # Retorna o indice na tupla da string passada no argumento

for elemento in tupla: # For que percorre cada indice da tupla
    print(elemento)

# LISTAS - [entre colchetes]

l1 = ['Homo sapiens', 'Canis familiaris', 'Felis catus'] # Variável declarada com o valor entre colchetes
l2 = ['Xenopus laevis', 'Ailuropoda melanoleuca'] # Variável declarada com o valor entre colchetes
l3 = l1 + l2 # Retorna a concatenação de duas listas por meio do operador '+'
print(l3)

l2_2 = l2 * 2 # Retorna a lista com os elementos duplicados x vezes
print(l2_2)

print(l1[0:2]) # Retorna os elementos do range 0 até 2 -> indices (0, 1)

l1.append('Gorila gorila') # Adiciona um elemento ao final da lista
print(l1)

l1.remove('Felis catus') # Remove o elemento passado no argumento da lista
print(l1)

#del(l1)
#print(l1)

for item in l2_2: # For que percorre cada indice da lista
    print(item)
