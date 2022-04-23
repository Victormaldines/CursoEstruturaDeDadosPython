# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 14:56:40 2022

@author: vitu
"""

# MANIPULAÇÃO DE STRINGS

a = 'casaco'
print(a)

maiuscula = a.upper() # Retorna a string com todos os caracteres maiúsculos
print(maiuscula)

minuscula = a.lower() # Retorna a string com todos os caracters minúsculos
print(minuscula)

capital = a.capitalize() # Retorna a string com o apenas o primeiro caractere maiúsculo
print(capital)

metade_palavra = a[0:4] # Retorna parte do começo da string [0:4] => indice 0 até o indice 3
print(metade_palavra)

ultimas_letras = a[3:] # Retorna parte do final da string [3:] => indice 3 até o indice final
print(ultimas_letras)

b = a.replace('aco', 'inha') # Retorna a string com o primeiro argumento substituído pelo segundo
print(a)
print(b)

c = a.replace('o', 'a') # Retorna a string com o primeiro argumento substituído pelo segundo
print(c)

print(c.find('s')) # Procura e retorna (se for encontrado) o indice do caractere passado no argumento (caso não: retorna -1)

print(c.find('a'))  # Procura e retorna (se for encontrado) o indice do caractere passado no argumento (caso não: retorna -1)

print(c.find('z'))  # Procura e retorna (se for encontrado) o indice do caractere passado no argumento (caso não: retorna -1)

e = ' casaco '
print(len(e)) # Retorna a quantidade de caracteres de uma string

f = e.strip() # Remove espaços antes e depois de uma string
print(f)
print(len(f)) 

n1 = 14
n2 = 16
print(f'Dividindo {n1} por {n2} o resultado é {n1/n2}') # Interpolação de string [formatando]
 