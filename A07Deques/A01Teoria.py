'''
DEQUES - DOUBLE ENDED QUEUE
TEORIA

    Add element               Add element
    at rear                   at front
        \                      /
        v                     v
        10 15 20 30 40 50 60 70
        /                     \
       v                       v
    Remove element            Remove element
    from rear                 from front

    STACK
              Add/Remove
                  ^
                  |
                  v
        x x x x x x

    QUEUE
        Add      Remove
        |          ^
        v          |
        x x x x x x

    DEQUE
    Add/Remove   Add/Remove
        ^         ^
        |         |
        v         v
        x x x x x x

    * Suporta operações de pilhas e filas
    * Aplicações
        * Filas de prioridade
        * Agendamento de tarefas de vários processadores
        * O algoritmo de agendamento de trabalho furtivo é usado pela biblioteca Threading Building Blocks (TBB) da
        Intel para programação paralela

OPERAÇÕES
    * Adicionar no início
    * Adicionar no no final
    * Excluir do início
    * Excluir do final

    * Implementação estátiva x circular(recomendado)
    
'''