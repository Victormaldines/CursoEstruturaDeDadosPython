'''
INSERTION SORT
TEORIA

    * É cerca de duas vezes mais rápido que a ordenação pelo método da bolha e um pouco mais rápido que a ordenação por
    seleção em situações normais
    * Funcionamento
        * Há um marcador em algum lugar no meio do vetor
        * Os elementos à esquerda do marcador estão parcialmente ordenados (estão ordenados entre eles, porém não estão
        em suas posições finais)
        * Os elementos à direita do marcador não estão ordenados

        ex.:
               elemento
               marcado
                  *
        1 3 4 5 7 2 9 6 8

                  *
                  2
        1 3 4 5 7   9 6 8

                *
                2
        1 3 4 5 7   9 6 8

              *
              2
        1 3 4 5 7   9 6 8

            *
            2
        1 3 4 5 7   9 6 8

          *
          2
        1 3 4 5 7   9 6 8

        *
        2
        1 3 4 5 7   9 6 8

          *
          2
        1   3 4 5 7 9 6 8

        1 2 3 4 5 7 9 6 8

                    *
        1 2 3 4 5 7 9 6 8

    * Na primeira passagem, é comparado no máximo um item. Na segunda passagem, máximo de dois itens, etc.
        * 1 + 2 + 3 + ... + N - 1 ~= N*(N-1)/2

    * Como em cada passagem uma média de apenas metade do número máximo de itens é de fato comparada antes do ponto de
    inserção ser encontrado, então comparações:
        * N*(N-1)/4

    * O número de cópias é aproximadamente o mesmo que o número de de comparações.

    * Para dados aleatórios, esse algoritmo executa duas vezes mais rápido que o método da bolha e mais rápido que a
    ordenação por seleção.

    * Para dados que já estejam quase ordenados esse algoritmo é ainda mais eficiente.

    * Para dados em ordem inversa, todas as comparações e deslocamentos são executados, sendo mais lento que o método da
    bolha.
'''