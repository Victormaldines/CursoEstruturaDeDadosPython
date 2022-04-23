"""
VETORES ORDENADOS
    * Os dados estão organizados na ordem ascendente de valores-chave, ou seja, com o menor valor no índice 0 e cada
    célula mantendo um valor maior que a célula abaixo
    * Vantagem: agiliza os tempos de pesquisa
        1 2 4 5 8 _ _

    INSERÇÃO
        3 ~> 1 2 4 5 _ _ _                  1 2 4 5 _ _ _
             1 2 4 _ 5 _ _  <- Teoria       1 2 4 5 5 _ _
             1 2 _ 4 5 _ _    Prática ->    1 2 4 4 5 _ _
             1 2 3 4 5 _ _                  1 2 3 4 5 _ _

        * Pesquisar uma média de N/2 elementos (pesquisa linear)
            * Pior caso: N
        * Mover os elementos restantes (N/2 passos)
            * Pior caso: N
        * Big-O - O(2n) = O(n)

    PESQUISA LINEAR
         * A pesquisa termina quando o primeiro item maior que o valor de pesquisa é atingido
         * Como o vetor está ordenado, o algoritmo sabe que não há necessidade de procurar mais
         * Pior caso: se o elemento não estiver no vetor ou na última posição
         * Big-O - O(n)
         * Visualização on-line: https://www.cs.usfca.edu/~galles/visualization/Search.html

    EXCLUSÃO
        4 ~> 1 2 4 5 8 _ _
             1 2 _ 5 8 _ _   <- Teoria      1 2 4 5 8 _ _
             1 2 5 _ 8 _ _     Prática ->   1 2 5 5 8 _ _
             1 2 5 8 _ _ _                  1 2 5 8 8 _ _

        * O algoritmo pode terminar na metade do caminho se não encontrar o item
        * Pesquisar uma média de N/2 elementos (pesquisa linear)
            * Pior caso: N
        * Mover os elementos restantes (N/2 passos)
            * Pior caso: N
        * Big-O O(2n) = O(n )
"""