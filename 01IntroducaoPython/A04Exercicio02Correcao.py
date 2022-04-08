# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:57:53 2022

@author: vitu
"""

tempo = float(input('Digite o tempo gasto na viagem: '))
velocidade = float(input('Digite a velocidade média: '))

distancia = tempo * velocidade
litros_usados = distancia / 12

print('Velocidade média:', velocidade)
print('Tempo gasto na viagem:', tempo)
print('Distância percorrida:', distancia)
print('Quantidade de litros:', litros_usados)
