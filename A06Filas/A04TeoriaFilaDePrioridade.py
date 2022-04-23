'''
FILA DE PRIORIDADE
TEORIA

* Os itens são ordenados por valor-chave, de modo que o item com a chave mais baixa/alta esteja sempre na frente
* Elementos de alta prioridade são colocados no início da fila, de média prioridade no meio da fila e elementos de baixa
prioridade no final da fila
    Priority Queue
        3- dequeue
         3 2 1 1 1
          3+ enqueue

Exemplo:
Números menores -> Maior prioridade

* Início
+ Final

+*
 _ _ _ _

+
*
7 _ _ _ Entra o número 7

* +
5 7 _ _ Entra o número 5

*   +
5 _ 7 _ Entra o número 6 (1/2)

*   +
5 6 7 _ Entra o número 6 (2/2)

*     +
1 5 6 7 Entra o número 1

  *   +
_ 5 6 7 Sai o número 1
'''