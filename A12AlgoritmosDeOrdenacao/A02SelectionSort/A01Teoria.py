'''
SELECTION SORT
TEORIA

* Melhora a ordenação pelo método da bolha reduzindo o número de trocas necessárias de N² para N
* O número de comparações permanece N²/2
* Funcionamento
    * Percorrer todos os elementos e selecionar o menor
    * O menor elemento é trocado com o elemento da extremidade esquerda do vetor (posições iniciais)
    * Os elementos ordenados acumulam-se na esquerda

* Algoritmo com 10 elementos faz 9 comparações na primeira passagem, 8 na segunda, 7 na terceira, etc (n-1, n-2, n-3).
    Para 10 itens:
        * 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45
* Big-O: O(n²)
* O algoritmo faz cerca de N²/2 comparações (mesmo número de comparações que o método da bolha)
* Com 10 elementos, são requeridas menos de 10 trocas (geralmente é feita uma troca a cada passagem)
* Com 100 itens, são requeridas 4.950 comparações, mas menos de 100 trocas
'''