# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:36:57 2022

@author: vitu

1. Leia a idade do usuário e classifiqueo-em:
    Criança - 0 a 12 anos
    Adolescente - 0 a 13 anos
    Adulto - acimda de 18 anos
    Se o usuário digitar um número negativo, mostrar a mensagem a idade é
    inválida
"""

idade = int(input('Informe a sua idade: '))

if idade > 0 and idade <= 12:
    print('Criança')
elif idade > 12 and idade < 18:
    print('Adolescente')
elif idade >= 18:
    print('Adulto')
else:
    print('Idade inválida')
