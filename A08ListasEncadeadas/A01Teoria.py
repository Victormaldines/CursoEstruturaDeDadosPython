'''
LISTAS ENCADEADAS
TEORIA

DESVANTAGENS VETORES
    * Em um vetor não ordenado, a busca é lenta
    * Em um vetor ordenado, a inserção é lenta
    * Em ambos, a remoção é lenta
    * O tamanho do vetor "não pode" ser alterado depois de ter sido criado
    * Mesmo vazios ocupam espaço na memória

LISTAS ENCADEADAS - NÓS

            Cabeça                                                     cauda
                \                                                       /
                (Obj|end-)-next->(Obj|end-)-next->(Obj|end-)-next->(Obj|end-)-...->


                    (vetor)       (lista)
LISTAS ENCADEADAS - POSIÇÃO  x RELACIONAMENTO

    * Vetor (posição)
        * Cada item ocupa uma certa posição
        * Cada posição pode ser acessada usando um número de índice
            elementos: 7 6 5 1
            indices:   0 1 2 3

    * Lista (relacionamento)
        * A única maneira de encontrar um elemento é seguir a sequência de elementos
        * Um item de dados não pode ser acessado diretamente, ou seja, o relacionamento entre eles deve ser utilizado
        * Inicia com o primeiro item, vai para o segundo, então o terceiro, até encontrar o item pesquisado

            Cabeça                                                     cauda
                \                                                       /
                (Obj|end-)-next->(Obj|end-)-next->(Obj|end-)-next->(Obj|end-)-...->

                Obj: Objeto
                end: Endereço
                next: Referência ao endereço do objeto subsequente

        * Cada elemento da lista é armazenado em um objeto
        * Cada elemento da lista referencia o próximo e só é alocado dinamicamente quando é necessário
        * Para referenciar o primeiro elemento é utilizado um elemento chamado cabeça da lista
            Cabeça
                \
                (Obj|end-)-next->(Obj|end-)-...->

        Exemplo: (info|proximo)
            (end) Cabeça de lista
                \
                (5|end-)-next->(4|end-)-next->(3|end-)-next->null

LISTAS ENCADEADAS SIMPLES

    Exemplo: (info|proximo-)->

        (end) Cabeça de lista
            \
            (5|end-)-next->(4|end-)-next->(3|end-)-next->null

    OPERAÇÕES
        * Insere no início
        * Excluir do início
        * Mostrar lista
        * Pesquisar
        * Excluir da posição

        * INSERE NO INÍCIO
            * Insere um novo nó no início da lista
            * É o local mais fácil para inserir um nó
            * O próximo deste novo elemento deve ser o primeiro da lista
            * A cabeça da lista aponta para o novo elemento

                (end)
                    \
                    (4|end-)-next->(3|end-)-next->null

                (5|end) ~> Novo nó criado

                (end)
                  |    (4|end-)-next->(3|end-)-next->null
                  |    /
                (5|end)

                ___________________________________________________________________

                (end)
                  |     (4|end-)-next->(3|end-)-next->null
                  |    /
                (5|end)

                (6|end) ~> Novo nó criado

                (end)
                  |    (5|end-)-next->(4|end-)-next->(3|end-)-next->null
                  |   /
                (6|end)

        * EXCLUIR DO INÍCIO
            * É o inverso do insere no início
            * Desconecta o primeiro nó roteando de novo o primeiro para apontar para o segundo nó
            * O segundo nó é encontrado por meio do campo próximo do primeiro nó

            (end)
                \
                (5|end-)-next->(4|end-)-next->(3|end-)-next->( |null)

            (end) _________
                           \
                (5|end-)-next->(4|end-)-next->(3|end-)-next->null

            (O <proximo> do Nó Cabeça recebe o <próximo> do primeiro objeto)

        * MOSTRAR LISTA E PESQUISAR
            * Para exibir a lista, deverá ser iniciado no primeiro elemento, seguindo a sequência de referências de nó em nó
            * O final da lista é indicado pelo campo próximo no último nó apontando para null/none ao invés de outro nó
            * Os nós são percorridos e é verificado se o valor do elemento é aquele que está sendo procurado
            * Se atingir o final da lista sem encontrar o nó desejado, finaliza sem encontrar o elemento

        * EXCLUIR DA POSIÇÃO
           * O nó a ser eliminado deve ser localizado (pesquisa)
           * Quando elimina o nó atual, terá que conectar o nó anterior ao nó seguinte

            Ex.:
                Excluir: 4
                (end)
                    \
                    (6|end-)->next->(5|end-)-next->(4|end-)-next->(3|end-)-next->null
                                 ObjAnterior(5)  ObjAtual(4)
                                                  (apagar)

                (end)                     ___next___
                    \                   /           \
                    (6|end-)-next->(5|end) (4|end-)-next->(3|end-)-next->null
'''