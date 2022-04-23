# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 14:08:29 2022

@author: vitu

1. Crie um arquivo .py com duas funções:
    - Função para ler um string (recebe como parâmetro uma mensagem e retorna
    o que o usuário digitou)
    - Função para ler um número float (recebe como parâmetro uma mensagem e
    retorna o que o usuário digitou)
"""

import A18Exercicio01Aux as ex

mensagem = input('Digite uma mensagem: ')
ex.imprimeString(mensagem)

numero = float(input('Digite um número: '))
ex.imprimeNumero(numero)
