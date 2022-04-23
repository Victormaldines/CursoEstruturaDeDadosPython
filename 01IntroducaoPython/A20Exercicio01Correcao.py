# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 15:01:22 2022

@author: vitu
"""

lista = []

try:
    lista.append(float(input('Digite o primeiro valor: ')))
    lista.append(float(input('Digite o segundo valor: ')))
    divisao = lista[0] / lista[2]
except ValueError:
    print('Erro! Valor inválido')
except ZeroDivisionError:
    print('Erro! Divisão por zero')
except IndexError:
    print('Erro! Índice inválido')
except KeyboardInterrupt:
    print('\nUsuário interrompeu a execucao')
else:
    print(f'A divião é {divisao}')
