# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 13:22:50 2022

@author: vitu

MÓDULOS ÚTEIS - RANDOM e TIME
"""

# RANDOM
# https://docs.python.org/3/library/random.html

print('\nBIBLIOTECA RANDOM\n')
import random # Importa a biblioteca random

print(random.random()) # Retorna um número float randômico entre 0 e 1

print(random.randint(1, 10)) # Retorna um número inteiro randômico entre 1 e 10

print(random.randrange(0, 10, 2)) # Retorna um número inteiro randômico entre 0 e 10 com passo 2 {0, 2, 4, 6, 8, 10}
print(random.randrange(1, 10, 2)) # Retorna um número inteiro randômico entre 1 e 10 com passo 2 {1, 3, 5, 7, 9}

x = ['K', 'd', 13, '34-j', 'x']
print(x)

print(random.choice(x)) # Retorna um elemento randômico da lista

# TIME
# https://docs.python.org/3/library/time.html
print('\nBIBLIOTECA TIME\n')

import time as tm # Importa a biblioteca time e atribui um alias 'tm'

print(tm.time()) # Retorna o tempo atual em segundos desde a Epoch (Era Unix -> datetime.datetime(1970, 1, 1, 0, 0, 0))

"""
Algoritmo: linhas: 40-47
calcula o tempo que o 'programa' demorou para executar
"""
antes = tm.time()
lista = []
for i in range(0, 10000):
    lista.append(i)
depois = tm.time()

intervalo = depois - antes
print(f'tempo: {intervalo} segundos')

print()

print('Finalizando...')
tm.sleep(2) # Para a execução com código .sleep(<x>) segundos
print('...')
tm.sleep(2)
print('Até a próxima')
