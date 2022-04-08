# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 11:29:02 2022

@author: vitu


VARIÁVEIS E CONSTANTES
    Por meio de variáveis que um algoritmo "guarda" os dados do problema
    Todo dado que tem a possibilidade de ser alterado no decorrer do tempo deverá ser tratado como uma variável
    Quando um dados não tem nenhuma possibilidade de variar no decorrer do tempo, deverá ser tratado como constante
    
Exemplo: calcular a área do triângulo. Sabemos que a fórmula para o cálculo da área do triângulo é BASE * ALTURA / 2. Base
e altura são dados que irão variar no decorrer do "tempo de execução". O número 2 da fórmula é um dado constante, pois
sempre terá o mesmo valor

TIPOS DE VARIÁVEIS
    Inteiros: valores positivos ou negativos, que não possuem parte fracionária.
        Exemplos: 1, 30, 40, 12
    Float: valores positivos ou negativos, que podem possuir uma parte fracionária (também podem ser inteiros).
        Exemplos: 1.4, 6.7, 10.3, 100, -47
    Caracteres (char ou string): qualquer elemento presente no teclado.
        Exemplos: "Maria", "João", 'M', 'F'
    Lógico (booleano): verdadeiro ou falso.
        Exemplos: true, false, 1, 0
"""

# VARIÁVEIS INTEIRAS
numero = -3
numero_jogos = 14
numero_convidados = 15

#print(numero, numero_convidados)

# VARIÁVEIS FLOAT (ponto flutuante)
pi = 3.14
numero_euler = 2.71
escala_terremoto = -4.55

#print(pi, numero_euler, escala_terremoto)

# STRING E CHAR
letra = 'a'
palavra1 = 'linguagem de programação'
palavra2 = 'Python'

#print(letra, palavra1, palavra2)
#print('Estou aprendendo uma', palavra1)
#print('Esta', palavra1, 'se chama', palavra2)

# INPUT
idade = int(input('Digite sua idade: '))
print('Sua idade é:', idade)

pH = float(input('Qual o pH do solo durante a última medição? '))
print('O pH medido foi', pH)

nome = str(input('Qual o seu nome? '))
print('Seu nome é', nome)