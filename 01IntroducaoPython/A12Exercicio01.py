# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 17:16:12 2022

@author: vitu

1. Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros
e os armazene dentro de uma lista. Após a leitura, crie outra estrutura para
somar todos os valores digitados
"""

numeros = []
for i in range(0, 5):
    numeros.append(int(input(f'Informe o {i+1}º número: ')))
    
soma = 0
for numero in numeros:
    soma += numero
print(soma)
    