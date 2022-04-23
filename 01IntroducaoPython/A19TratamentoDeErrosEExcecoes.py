# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 14:28:23 2022

@author: vitu
TRATAMENTO DE ERROS E EXCECOES
    * NameError: variável não foi definida
    * TypeError: tipos de dados incompativeis
    * RuntimeError: erro de execucao
    * SyntaxError: sintaxe digitada é inválida e não reconhecida
    pelo interpretador
    * ZeroDivisionError: divisão por zero
    * IndexError: indice está fora da colecao
"""

# TIPOS DE ERROS
# print('Meu nome é', nome) # NameError

# (3 / 0 # ZeroDivisionError

# 2.3 / 'cachorro' # TypeError

# c = [1, 2, 3, 4, 5]
# c[5] # IndexError

# TRATAMENTO DOS ERROS

'''
while True:
    try: # Verifica se há exceções escopo do bloco try
        n = int(input('Digite um número inteiro: '))
    except: # Se houver alguma exceção no escopo do bloco try, executa o bloco except
        print('Valor inválido')
    else: # Se NÃO houver nenhuma exceção no escopo do bloco try, executa o bloco else
        print(f'O valor digitado é {n}')
        break
'''

while True: 
    try: # Verifica se há exceções no escopo do bloco try
        p = int(input('Digite um número inteiro: '))
    except ValueError: # Se houver alguma exceção d ValueError (Valor inválido) no bloco try, executa o bloco except ValueError
        print('Valor inválido')
    except KeyboardInterrupt: # Se houver alguma excessão de KeyboardInterrupt (Usuário interrompe execução do programa) no bloco try, executa o bloco except KeyboardInterrupt
        print('\nUsuário interrompeu a execução')
        break # Interrompe o laço infinito
    else:
        print(f'Valor digitado é {p}')
        break # Interrompe o laço infinito