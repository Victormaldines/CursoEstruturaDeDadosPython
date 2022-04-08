# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 18:43:03 2022

@author: vitu
"""

def leitura():
    tempo = float(input('Digite o tempo da viagem: '))
    velocidade = float(input('Digite a velocidade: '))
    return tempo, velocidade

def calcula_distancia(tempo, velocidade):
    return tempo * velocidade

def calcula_litros(distancia):
    return distancia / 12

def imprime(velocidade, tempo, distancia, litros):
    print('Velocidade:', velocidade)
    print('Tempo:', tempo)
    print('Distância:', distancia)
    print('Litros:', litros)
    
t, v = leitura()
d = calcula_distancia(t, v)
l = calcula_litros(d)
imprime(v, t, d, l)
