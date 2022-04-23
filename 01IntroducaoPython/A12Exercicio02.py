# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 17:20:13 2022

@author: vitu

2. Crie um dicionário para armazenar o nome e a nota de 3 alunos, fazendo a
leitura dos valores por meio de uma estrutura de repetição. Depois, crie
uma nova estrutura de repetição para somar todas as notas e retornar a média.
"""

alunos = {}

for i in range(0, 3):
    nome = str(input(f'Informe o nome do {i+1}º aluno: '))
    nota = float(input(f'Informe a nota do {i+1}º aluno: '))
    
    alunos.update({nome: nota})
    
print(alunos)

soma = 0
for nome, nota in alunos.items():
    soma += nota

print(soma / len(alunos))
