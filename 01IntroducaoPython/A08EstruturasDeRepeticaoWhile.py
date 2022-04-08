# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 22:29:42 2022

@author: vitu

ESTRUTURA DE REPETIÇÃO - WHILE
"""
# WHILE

numero = 1

while numero < 6:
    print(numero)
    numero += 1
print('---')

numero = 5

while numero > 0:
    print(numero)
    numero -= 1
    
# 1 + 2 + 3 + 4 + 5
soma = 0
numero = 1
while numero < 6:
    soma += numero
    numero += 1
print(soma)

numero = -1
while numero < 1 or numero > 10:
    numero = int(input('Digite um número de 1 a 10: '))
