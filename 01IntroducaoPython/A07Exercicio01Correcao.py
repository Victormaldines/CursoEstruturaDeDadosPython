# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 17:05:21 2022

@author: vitu
"""

idade = int(input('Digite a idade: '))

if idade >= 0 and idade <= 12:
    print('Criança')
elif idade > 12 and idade <= 18:
    print('Adolescente')
elif idade > 18:
    print('Adulto')
else:
    print('Idade inválida')