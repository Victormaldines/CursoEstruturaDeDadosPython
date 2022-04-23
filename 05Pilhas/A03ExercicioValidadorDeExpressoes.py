'''
PILHAS - EXERCÍCIO
VALIDADOR DE EXPRESSÕES

* Os delimitadores são as chaves { e }, os colchetes [ e ] e os parênteses ( e )
* Cada delimitador de abertura ou à esquerda deve ser casado com um delimitador de fechamento ou à direita
* Toda { deve ser seguida por uma } que case com ela

* Exemplos
    * c[d] ~> correto
    * a{b[c]d}e ~> correto
    * a{b(c]d}e ~> incorreto - ] não casa com (
    * a[b{c}d]e} ~> incorreto - nada casa com } no final
    * a{b(c) ~> incorreto - nada casa com { de abertura

Caractere lido  | Conteúdo da pilha
a               |
{               | {
b               | {
(               | {(
c               | {(
[               | {([
d               | {([
]               | {(
e               | {(
)               | {
f               | {
}               |
'''

import numpy as np

class Pilha:

    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=str)

    def __pilha_cheia(self):
        if self.__topo == self.__capacidade -1:
            return True
        return False

    def __pilha_vazia(self):
        if self.__topo == -1:
            return True
        return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
            print('Pilha está cheia')
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor

    def desempilhar(self):
        if self.__pilha_vazia():
            print('Pilha está vazia')
        else:
            self.__topo -= 1

    def ver_topo(self):
        if self.__topo != -1:
            return self.__valores[self.__topo]
        return -1

def recebe_expressao():
    expressao = str(input('Informe a expressão: '))
    return expressao

def gera_capacidade_pilha(expressao):
    tamanho = 0
    for letra in expressao:
        if letra == '{' or letra == '[' or letra == '(':
            tamanho += 1
    return tamanho

def expressao_valida(expressao):
    capacidade = gera_capacidade_pilha(expressao)
    pilha = Pilha(capacidade)

    for letra in expressao:
        if letra == '{' or letra == '[' or letra == '(':
            pilha.empilhar(letra)
            continue
        if letra == '}':
            if pilha.ver_topo() == '{':
                pilha.desempilhar()
            else:
                return 'Expressão inválida'
        elif letra == ']':
            if pilha.ver_topo() == '[':
                pilha.desempilhar()
            else:
                return 'Expressão inválida'
        elif letra == ')':
            if pilha.ver_topo() == '(':
                pilha.desempilhar()
            else:
                return 'Expressão inválida'
    if pilha.ver_topo() == -1:
        return 'Expressão Válida'
    return 'Expressão inválida'

while True:
    expressao = recebe_expressao()
    print(expressao_valida(expressao))
    print()