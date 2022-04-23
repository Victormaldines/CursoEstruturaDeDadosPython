'''
LISTAS ENCADEADAS COM EXTREMIDADES DUPLAS
TEORIA

    * Para inserir um nó no final d e uma lista com extremidade simples, é necessário percorrer todos os elementos
    * A referência para o último nó permite inserir um novo nó diretamente no final da lista, assim como no início
    * Operações
        * Inserir no início
        * INSERIR NO FINAL (adicional)
        * Excluir do início

Big-O
    Inserir no início, no final e exclusão ~> O(1) - Constante
        * utilizando listas com extremidades duplas, tais operações são muito rápidas
            - tempo O(1)
    Localizar, eliminar ou inserir próximo a um item específico ~> O(n) - Linear
        * Requer buscar, em média, metade dos itens - requer O(N) comparações. Semelhante a um vetor, porém, na lista
        encadeada não é necessário mover itens

* Utiliza somente a memória que necessitar, podendo ser expandida de acordo com o aumento da lista
'''