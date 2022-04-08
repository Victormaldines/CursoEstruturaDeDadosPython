# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 17:44:08 2022

@author: vitu
"""

# 2. DICIONÁRIO
alunos = {}
for _ in range(1, 4):
    nome = input('Digite o nome: ')
    nota = float(input('Digite a nota: '))
    alunos[nome] = nota
    
soma = 0
for nota in alunos.values():
    soma += nota
    
print('Média:', soma / 3)
