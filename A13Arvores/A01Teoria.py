'''
ÁRVORES
ÁRVORE BINÁRIA

* Uma árvore combina as vantagens de duas estruturas: um vetor ordenado e uma lista encadeada
* Busca rápida (como em um vetor ordenado)
* Inserção e eeliminação rápida (ciomo em uma lista encadeada)

            2
          /  \
        7     5  <~ nó
      /  \     \  <~ aresta
    2     6     9
        /  \   /
       5   11 4

* Uma árvore consiste em nós (círculos) conectados por arestas (linhas)
* Máximo dois filhos
* Filho à esquerda e filho à direita
* Pode ter um ou nenhum filho

TERMINOLOGIA DE ÁRVORES
    * Caminho
        - Caminho que liga um nó até outro nó

    * Raiz
        - É o nó parte superior. Há apenas uma raiz em uma árvore e deve haver somente um caminho da raiz até qualquer
        outro nó

    * Pai
        - Qualquer nó (exceto o raiz) tem exatamente uma aresta que sobe para outro nó. O nó acima dele é chamado de pai
        do nó

    * Filho
        - Qualquer nó pode ter uma ou mais linhas descendo para outros nós. Esses nós abaixo de uma dado nó são chamados
        de seus filhos

    * Folha
        - Um nó que não tem filhos

    * Subárvore
        - Qualquer nó pode ser considerado como sendo a raiz de uma subárvore, que consiste em seus filhos

    * Visitando
        - Um nó é visitado quando o controle do programa chega ao nó, em geral para a finaldiade de executar alguma
        operação do nó

    * Percorrendo
        - Visitar todos os nós em alguma ordem específica

    * Níveis
        - O nível de um determinado nó refere-se a quantas gerações o nó está da raiz

    * Chaves
        - Valor usado para buscar um item

ÁRVORE BINÁRIA DE BUSCA
    * O filho à esquerda de um nó tem que ter uma chave menor que seu pai e o filho á direita de um nó tem que ter uma
    chave maior ou igual ao seu pai

            53
         /     \
       30        72
     /    \      / \
   14      39  61   84
  /  \    /  \     /
09   23  34 49   79
'''