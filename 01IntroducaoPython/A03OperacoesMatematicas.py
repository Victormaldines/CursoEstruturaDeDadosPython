# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:16:32 2022

@author: vitu

OPERAÇÕES MATEMÁTICAS
"""

# OPERAÇÕES MATEMÁTICAS
a = 5
b = 3

print(a, b)
print(a + b) # Soma a com b

print('A soma é', a + b) # Retorna a soma de a com b
print('A subtração é', a - b) # Retorna a subtração de a com b
print('A divisão é', a / b) # Retorna a divisão de a por b
print('A multiplicação é', a * b) # Retorna a multiplicação de a com b
print('O resto da divisão é', a % b) # Retorna o resto da divisão de a por b
print('5 elevado a 4 é', 5**4) # Retorna o valor de 5 elevado a 4
print(5 * 5 * 5 * 5)

import math # Importa a lib math -> necessária para efetuar a chamada de alguns métodos não-nativos do Python
print('A raiz quadrada de 81 é', math.sqrt(81)) # Acessa o objeto math, chama o método sqrt() -> retorna
                                                # a raiz quadrada do número passado no argumento

# ARREDONDAMENTO
casos_doenca = 134
numero_habitantes = 34432
casos_por_habitante = casos_doenca / numero_habitantes

print(casos_por_habitante)
print(round(casos_por_habitante, 6)) # Arredonda o primeiro argumento em x casas decimais; x -> segundo valor passado no argumento
print('O número de casos por habitante é de', round(casos_por_habitante, 4)) # Arredonda o primeiro argumento em x casas decimais
                                                                             # x -> segunda valor passado em x casas decimais