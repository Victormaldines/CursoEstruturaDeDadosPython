# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 12:44:20 2022

@author: vitu

MÓDULOS ÚTEIS - MATH e DATETIME
"""

# BIBLIOTECA MATH
# https://docs.python.org/3/library/math.html

print('BIBLIOTECA MATH\n')
import math # Importa a biblioteca math

print(math.sqrt(9)) # Método que retorna a raiz quadrada do valor passado no parâmetro

print(math.sin(45)) # Método que retorna o seno do valor passado no parâmetro

print(math.cos(45)) # Método que retorna o cosseno do valor passado no parâmetro

print(math.log(1000, 10)) # Retorna o logaritmo de 1000 na base 10
print(math.log(32, 2)) # Retorna o logaritmo de 32 na base 2
print(math.log(1000)) # Valor default do segundo parâmetro é o número de Euler, bastante utilizado em operações logaritmicas
print(math.e) # Número de Euler
print(math.pi) # Número de Pi

# BIBLIOCA DATE
# https://docs.python.org/3/library/datetime.html
print('\nBIBLIOTECA DATETIME\n')
import datetime # Importa a biblioteca datetime
print(dir(datetime)) # Retorna os métodos/atributos disponíveis no objeto datetime

print(datetime.date.today()) # Retorna a data atual com base na data do sistema operacional
print(datetime.datetime.now()) # Retorna a data/horário com base na data/horário do sistema operacional

data = datetime.date(1980, 6, 10) # Instancia um objeto datetime com base nos argumentos de data passados no parâmetro da função
print(data) # Retorna a data (equivalente ao datetime.date.today())
print(data.month) # Retorna o mes do objeto instanciado
print(data.day) # Retorna o dia do objeto instanciado
print(data.year) # Retorna o ano do objeto instanciado

horario = datetime.datetime(1980, 7, 10, 7, 30, 0) # Instancia um objeto com base nos argumentos de data/horário passados no parâmetro da função
print(horario) # Retorna a data/horário

print(horario.hour) # Retorna o horário do objeto instanciado
print(horario.minute) # Retorna o(s) minuto(s) do objeto instanciado
print(horario.second) # Retorna o(s) segundo(s) do objeto instanciado
