# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:04:06 2022

@author: vitu
OPERADORES LÓGICOS E RELACIONAIS
"""

# OPERADORES LÓGICOS
a = True
b = False

print(a and b) # Retorna TRUE se TODAS as variáveis forem TRUE
print(a & b) # Retorna TRUE se TODAS as variáveis forem TRUE

c = a and b

print("'A' e 'B' é igual a:", c)

print(a or b) # Retorna TRUE se PELO MENOS uma das variáveis forem TRUE
print(a | b) # Retorna TRUE se PELO MENOS uma das variáveis forem TRUE

d = a or b

print("'A' ou 'B' é igual a:", d)

print(not a) # Retorna o valor lógico INVERSO. Ex.: True ~> False
print(not b) # Retorna o valor lógico INVERSO. Ex.: False ~> True

print('\n')
# OPERADORES RELACIONAIS

print(5 > 3) # Retorna TRUE se 5 for MAIOR que 3
print(5 < 3) # Retorna TRUE se 5 for MENOR que 3
print(5 > 5) # Retorna TRUE se 5 for MAIOR que 5
print(5 >= 5) # Retorna TRUE se 5 for MAIOR OU IGUAL a 5
print(5 <= 3) # Retorna TRUE se 5 for MENOR OU IGUAL a 3
print(5 == 3) # Retorna TRUE se 5 for IGUAL a 3
print(5 != 3) # Retorna TRUE se 5 for DIFERENTE de 3
