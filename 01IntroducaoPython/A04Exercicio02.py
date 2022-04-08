# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:50:53 2022

@author: vitu
"""

"""
2. Efetuar o cálculo da quantidade de litros de combustível gasto
em uma viagem, utilizando um automóvel que faz 12Km por litro.
Para obter o cálculo, o usuário deve fornecer o tempo gasto
na viagem e a velocidade média durante ela. Desta forma, será
possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VEL.
Tendo o valor da distância, basta calcular a quantidade de litros de
combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA * 12.
O programa deve apresentar os valores da velocidade média, tempo gasto na
viagem, a distância percorrida e a quantidade de litros utilizada na viagem
"""

KM_POR_LITRO = 12

tempo = float(input('Informe o tempo gasto na viagem (em horas): '))
velocidade = float(input('Informe a velocidade média durante a viagem (em km/h): '))
distancia = tempo * velocidade

litrosUsados = distancia / KM_POR_LITRO

print(combustivelGasto)
