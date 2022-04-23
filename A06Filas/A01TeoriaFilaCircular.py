'''
FILAS
TEORIA
FIFO - First-In-First-Out (Primeira-A-Entrar-Primeiro-A-Sair)

    * A primeira pessoa a entrar no final da fila será a primeira pessoa a chegar na frente da fila
    * É uma estrutura semelhante a uma pilha, exceto que em uma fila o primeiro elemento inserido é o primeiro a ser
    removido (First-In-First-Out, FIFO - Primeiro-A-Entrar-Primeiro-A-Sair)
    * Aplicações
        * Modela aviões aguardando para decolar
        * Pacotes de dados esperando para serem transmitidos pela rede
        * Fila da impressora, no qual serviços de impressão aguardam a impressora ficar disponível

OPERAÇÕES

    * Enfileirar
        colocar um elemento no final da fila
    * Desenfileirar
        remover um item do início da fila
    * Ver início da fila
        mostra o elemento que está no início da fila

FILA CIRCULAR
* Inicio
+ Final

*   +
6 2 5 _ ~> Frente: 6, Trás: 5

*     +
6 2 5 7 ~> Entra o número 7

  *   +
_ 2 5 7 ~> Sai o número 6

    * +
_ _ 5 7 ~> Sai o número 2

+   *
1 _ 5 7 ~> Entra o número 1

  + *
1 2 5 7 ~> Entra o número 2

  +   *
1 2 _ 7 ~> Sai o número 5

* +
1 2 _ _ ~> Sai o número 7
'''