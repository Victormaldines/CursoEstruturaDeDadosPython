# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:25:57 2022

@author: vitu

OPERADOR CONDICIONAL
"""

if 5 > 3:
    print('5 é maior que 3')
print('\n')

if 5 > 4:
    print('5 é maior')
else:
    print('5 não é maior')    
print('\n')

n = 9

if n == 4:
    print('n é igual a 4')
else:
    if n == 3:
        print('n é igual a 3')
    else:
        print('n não é igual a 4 nem 3')
print('\n')
        
x = 1
y = 5
if (x > 1) or (y % 2 == 0):
    print('x é maior que 1 e y é par')
else:
    print('Uma ou nenhuma das condições foram satisfeitas')
