# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 14:46:47 2022

@author: vitu
# COLEÇÕES
DICIONÁRIOS e CONJUNTOS (SET)
"""
# DICIONÁRIOS

coleta = {'Aedes aegypt': 32, 'Aedes albopictus': 22, 'Anopheles darlingi': 14} # Definição utilizando chaves com valores par key:value,
print(coleta['Aedes aegypt']) # Retorna o valor da chave 'Aedes aegypt'
coleta['Rhodnius montenegrensis'] = 11 # Adiciona ao dicionário a chave 'Rhodnius montenegrensis' com o valor 11
print(coleta)

del(coleta)['Aedes albopictus'] # Remove do dicionário o item com a chave 'Aedes albopictus'
print(coleta)

print()
print(coleta.items()) # Retorna um conjunto iterável de tuplas
print(coleta.keys()) # Retorna as chaves do dicionário
print(coleta.values()) # Retorna os valores do dicionário
print()

coleta2 = {'Anopheles gambie': 13, 'Anopheles daeneorum': 14}
print(coleta2)
coleta.update(coleta2)  # Adiciona, caso não já exista, o os itens do dicionário passado
                        # no argumento no dicionário que efetuou a chamada do método
print(coleta)
print()

print(coleta.items())
for especie, num_especimes in coleta.items(): # Loop for iterando sobre o dicionário -> cada elemento é uma tupla
    print(f'Espécie: {especie}, Número de especimes coletados: {num_especimes}')

print('\n')

# CONJUNTOS (SET)
biomoleculas = ('proteína', 'ácidos nucleicos', 'carboidrato', 'lipídeo',
                'ácidos nucleicos', 'carboidrato', 'carboidrato', 'carboidrato')

print(biomoleculas)

print(set(biomoleculas)) # Remove as duplicatas de uma tupla

c1 = {1, 2, 3, 4, 5}
c2 = {3, 4, 5, 6, 7}
c3 = c1.intersection(c2) # C1 ^ C2 # Retorna os números da interceção dos conjuntos c1 e c2
print(c3)

print(c1.difference(c2)) # C1 ^ ~C2 # Retorna os números da diferença dos conjuntos c1 e c2 =>  C1 ^ ~C2
print(c2.difference(c1)) # C2 ^~C1  # Retorna os números da diferença dos conjuntos c2 e c1 =>  C2 ^~C1
