'''
PILHAS
TEORIA

LIFO -> Last-In-First-Out
O último elemento a entrar na pilha é o primeiro a sair

Exemplo de pilha:
    Pilha de Moedas
        Para retirar a moeda do meio, será necessário remover as moedas que estão acima dessa moeda-objetivo
    Pilha de Pratos
        Para retirar o prato do meio, será necessário remover os pratos que estão acima desse prato-objetivo

Exemplo 'real':
    A - você está ocupado com um projeto de longo prazo
        Pilha ~> A
    B - é interrompido por um colega solicitando ajuda em um outro projeto
        Pilha ~> A B
    C - enquanto estiver trabalhando em B, alguém da contabilidade aparece para uma reuniãosobre despesas de viagem
        Pilha ~> A B C
    D - durante a reunião, recebe um telefonema de emergência de alguém de vendas e passa alguns minutos resolvendo um problema relacionado a um novo produto
        Pilha ~> A B C D
    Quando tiver terminado o telefonema D, voltará para a reunião C
        Pilha ~> A B C
    Quando tiver acabado com C, voltará para o projeto B
        Pilha ~> A B
    E quando tiver terminado com B, poderá finalmente votlar para o projeto A
        Pilha ~> A
    OBS: A pilha pode começar vazia e terminar vazia

ALGUMAS CARACTERÍSTICAS
    * Permite acesso a um item de dados: o último item inserido
    * Se o último item for removido, o item anterior ao último inserido poderá ser acessado

APLICAÇÕES
    * Correção de expressões aritméticas, tais como 3 * (4+5)
    * Percorrimento de uma árvore binária
    * Pesquisa do vértice de um grafo
    * Microprocessadores com arquitetura baseada em pilhas. Quando um método é chamado, seu endereço de retorno
    e seus parâmetros são empilhados em uma pilha e quando ele retorna, são desempilhados

OPERAÇÕES
    Empilhar
        Colocar um item de dados no topo da pilha
    Desempilhar
        Remover um item do topo da pilha
    Ver o Topo
        Mostra o elemento que está no topo da pilha
'''

