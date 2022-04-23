'''
SHELL SORT (Shell é o nome de quem o elaborou)
TEORIA

Melhora a ordenação por inserção, podendo ser considerado uma "versão" do insertion sort

Funcionamento
    * O vetor original é quebrado em subvetores
    * Cada subvetor é ordenado comparando e trocando os valores
    * Ao final de uma rodada, o subvetor é quebrado em mais um vetor
    * Vetor com 20 elementos:
        * Primeira rodada: 10 elementos
        * Segunda rodada: 5 elementos
        * Terceira rodada: 2/3 elementos

        N / 2

        8 5 1 4 2 3

        *     *
        8 5 1 4 2 3 (esquerda maior que o da direta? swap : dontSwap)
        4 5 1 8 2 3

          *     *
        4 5 1 8 2 3
        4 2 1 8 5 3

            *     *
        4 2 1 8 5 3
        4 2 1 8 5 3

        *   *   *
        4 2 1 8 5 3
            *   *
        1 2 4 8 5 3
        1 2 4 8 5 3

          *   *   *
        1 2 4 8 5 3
              *   *
        1 2 4 8 5 3
        1 2 4 3 5 8

        * * * * * *
        1 2 4 3 5 8
          * * * * *
        1 2 4 3 5 8
            * * * *
        1 2 4 3 5 8
              * * *
        1 2 3 4 5 8
                * *
        1 2 3 4 5 8

* A complexidade do algoritmo depende dos intervalos escolhidos
* Pior caso: O(n²)
* Melhor caso: O(n*log n)
* Melhor do que o selection sort O(n²) e que o bubble sort O(n²)
* Considerado um algoritmo "instável" porque não examina os elementos dentro de um intervalo
'''