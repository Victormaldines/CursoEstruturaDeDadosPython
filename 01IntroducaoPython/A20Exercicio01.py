# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 14:49:07 2022

@author: vitu
1. Crie uma lista vazia e faça a leitura de dois valores do tipo float,
colocando cada um dos valores nas primeiras posições da lista (o valor 1
ficará na posição 0 da lista e o valor2 ficará na posicao 1 da lista). Faça a
divisão dos dois valores e trate as seguintes exceções:
    - ValueError: se o usuário digitar um caractere inválido
    - ZeroDivisionError: Se o usuário digitar zero e ocorrer erro na divisão
    - IndexError: Caso a divisão seja feita levando em consideração posições
    que não existem na lista
    - KeyboardInterrupt: caso o usuário interrompa a execução

2. Mostre uma mensagem personalizada na ocorrência de cada um desses erros
"""

lista = []

while True:
    try:
        lista.append(float(input('Digite o primeiro valor: ')))
        lista.append(float(input('Digite o segundo valor: ')))
        
        res = lista[0] / lista[1]
    except ValueError:
        print('Um dos valores é inválido')
    except ZeroDivisionError:
        print('Não é possível dividir o valor escolhido por zero')
    except IndexError:
        print('Valor fora da coleção')
    except KeyboardInterrupt:
        print('\nUsuário interrompeu a excecução')
        break
    else:
        print(res)
        break
