# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 18:04:33 2022

@author: vitu

1. Ler uma temperatura em graus Celsius e apresentá-la convertida em graus
Fahrenheit. A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a
temperatura em Fahrenheit e C é a temperatura em graus Celsius
    - Função para ler e retornar o valor da temperatura (não recebe parâmetro)
    - Função para fazer o cálculo (Recebe como parâmetro a temperatura em graus
    Celsius)
    - Função para mostrar o resultado, recebendo como parâmetro o valor e
    fazendo a impressão
"""

def leRetornaTemperatura():
    temperatura = float(input('Informe a temperatura em °C: '))
    return temperatura

def calculaCelsiusParaFahrenheit(celsius):
    fahrenheit = (9 * celsius + 160) / 5
    return fahrenheit

def mostraResultado(resultado):
    print(resultado)

#mostraResultado(calculaCelsiusParaFahrenheit(leRetornaTemperatura()))

temperaturaCelsius = leRetornaTemperatura()
temperaturaFahrenheit = calculaCelsiusParaFahrenheit(temperaturaCelsius)
mostraResultado(temperaturaFahrenheit)
