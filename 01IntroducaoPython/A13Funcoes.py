# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 17:44:45 2022

@author: vitu

FUNÇÕES
"""

# FUNÇÃO SEM PARÂMETRO E SEM RETORNO
def mensagem(): # Define a função 'mensagem'
    print('Texto da função')

mensagem() # Invoca a função 'mensagem'
mensagem() # Invoca a função 'mensagem'
mensagem() # Invoca a função 'mensagem'

# FUNÇÃO COM PASSAGEM DE PARÂMETROS

def mensagem(texto): # Define a função 'mensagem' com passagem de parâmetro 'texto'
    print(texto)
    
mensagem('Texto 1') # Invoca a função 'mensagem'
mensagem('Texto 2') # Invoca a função 'mensagem'
mensagem('Texto 3') # Invoca a função 'mensagem'

def soma(a, b): # Define a função 'soma' com passagem de parâmetros 'a' e 'b'
    print(a + b)
    
soma(2, 3) # Invoca a função 'soma'
soma(3, 3) # Invoca a função 'soma'
soma(1, 2) # Invoca a função 'soma'
print()

# FUNÇÃO COM PASSAGEM DE PARÂMETROS E RETORNO
def soma(a, b): # Define a função 'soma' com passagem de parâmetro 'a' e 'b' e retorno 'a+b'
    return a + b

print(soma(3, 2)) # Printa o valor retornado da função 'soma'
r = soma(3, 2) # Atribui a uma variável o valor retornado da função 'soma'

print(r)

def calcula_energia_potencial_gravitacional(m, h, g = 10): # Define uma função com parâmetros required e opcionais (com valor default)
    ''' Descrição da função:
    Calcula a energia potencial gravitacional
    m: massa, entrada como uma variavel float
    h: altura, entrada como uma variavel float
    
    Argumento opcional:
    g: aceleração gravitacional, com valor default de 10
    '''
    e = g * m * h
    return e

print(calcula_energia_potencial_gravitacional(30, 12)) # Printa o retorno da função passando apenas os valores required
resposta = calcula_energia_potencial_gravitacional(30, 12, 9.8) # Atribui a uma variável o retorno da função passando todos os parâmetros
print(help(calcula_energia_potencial_gravitacional)) # help(<funcao>) retorna a documentação personalizada da função no parâmetro
