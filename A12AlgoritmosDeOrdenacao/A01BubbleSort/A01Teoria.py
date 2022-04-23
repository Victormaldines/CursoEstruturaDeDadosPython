'''
ALGORITMOS DE ORDENAÇÃO

    Após uma base de dados estar construída, pode ser necessário ordená-la, como:
        * Nomes em ordem alfabética
        * Alunos por nota
        * Clientes por CEP
        * Vendas por preço
        * Cidades em ordem crescente de população
    Ordenar dados pode ser um passo preliminar para pesquisá-los
    (pesquisa binária X pesquisa linear)

BUBBLE SORT
TEORIA

    * Notavelmente lento e é o mais simples dos algoritmos de ordenação
    * Funcionamento
        * Comparação de dois números
        * Se o da esquerda for maior, os elmentos devem ser trocados
        * Desloca-se uma posição à direita
    * À medida que o algoritmo avança, os itens maiores "surgem como uma bolha" na extremidade superior do vetor
    * Visualização online: https:://visualgo.net/en/sorting

    * O algoritmo com 10 elementos faz 9 comparações na primeira passagem, 8 na segunda, 7 na terceira, etc (n-1, n-2,
    n-3).
        Para 10 itens:
            9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1
    * Big-O: O(n²)
    * O algoritmo faz cerca de N²/2 comparações
    * Há menos trocas do que há comparações, pois dois elementos serão trocados somente se precisarem
    * Se os dados forem aleatórios, uma troca será nacessária mais ou menos N²/4 (no pior caso, com os dados em modo
    inverso, uma troca será necessária a cada comparação)

    Exemplo:

        10 elementos

    Comparações
    N²/2
    10²/2
    100/2
    50
    aproximadamente 50 comparações

    Trocas
    N²/4
    10²/4
    100/4
    25
    aproximadamente 25 trocas

    passos trocas
    passos = 3
    trocas * passos
    25 * 3
    75
    aproximadamente 75 passos em trocas

    passos comparações
    passos = 1
    comparações * passos
    50 * 1
    50
    aproximadamente 50 passos em comparações

    total passos aproximados: 125
'''