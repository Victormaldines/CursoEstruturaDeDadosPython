# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 22:57:06 2022

@author: vitu
"""

# FOR

nota = media = soma = 0

for _ in range(1, 6):
    nota = float(input('Digite a nota: '))
    soma += nota
media = soma / 5
print('A média é', media)

"""
# WHILE
nota = soma = 0
numero = 1
while numero <= 5:
    nota = float(input('Digite a nota: '))
    soma += nota
    numero += 1
print('A média é', soma / 5)
"""
