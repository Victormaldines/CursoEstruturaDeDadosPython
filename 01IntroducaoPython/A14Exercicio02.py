# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 18:21:49 2022

@author: vitu

2. Efetuar o cálculo da quantidade de litros de combustível gasto em uma
viagem, utilizando um automóvel que faz 12Km/l. Para obter o cálculo, o usuário
deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta
forma, será possível obter a distância percorrida com a fórmula s = t * v.
Tendo o valor da distância, basta calcular a quantidade de litros de
combustível utilizada na viagem, com a fórmula: litros_usados = s / 2. O
programa deve apresentar os valores da velocidade média, tempo gasto na viagem
a distância percorrida e a quantidade de litros utilizada na viagem
    - Função para ler os valores (não recebe parâmetro e retorna os dois
    valores)
    - Função para calcular a distância (recebe como parâmetro o tempo e a
    velocidade e retorna a distancia)
    - Função para calcular a quantidade de litros (recebe como parâmetro a
    distância e retorna os litros)
    - Função para apresentar o resultado (recebe como parâmetro os valores e
    somente imprime o resultado)
"""

def leTempoGastoEVelocidadeMedia():
    tempoGasto = float(input('Informe o tempo gasto na viagem: '))
    velocidadeMedia = float(input('Informe a velocidade média: '))
    return [tempoGasto, velocidadeMedia]

def calculaDistancia(t, v):
    distancia = t * v
    return distancia

def calculaQuantidadeLitros(distancia):
    KM_POR_LITROS = 12
    quantidadeLitros = distancia / KM_POR_LITROS
    return quantidadeLitros
    
def imprimeResultado(resultado):
    print(resultado)

resultado = leTempoGastoEVelocidadeMedia()
tempo = resultado[0]
velocidade = resultado[1]

distancia = calculaDistancia(tempo, velocidade)

quantidadeLitros = calculaQuantidadeLitros(distancia)

imprimeResultado(quantidadeLitros)
