"""
MERGE SORT
TEORIA

* Um dos algoritmos de ordenação mais populares

* FUNCIONAMENTO
    * Divisão do problema em subproblemas (dividir e conquistar)
    * Divide o vetor continuamente pela metade, ordena e combina (merge)

    |38|27|43|3|9|82|10|
    |30|27|43|3| // |9|82|10|
    |30|27| / |43|3| // |9|82| / |10|
    |30| / |27| / |43| / |3| // |9| / |82| / |10|
       \   /
    |27|30| / |43| / |3| // |9| / |82| / |10|
                \    /
    |27|30| / |3|43| // |9| / |82| / |10|
       \       /
    |3|27|
    |3|27|30|43| // |9| / |82| / |10|
                     \            /
    |3|27|30|43| // |9|10| / |82| 
    |3|27|30|43| // |9|10|82|
          \            /
       |3|9|10|27|30|43|82|

* O Pior caso: O(n*log n)
* Melhor caso: O(n*log n)
* Melhor caso do que o bubble sort O(n²), que o selection sort O(n²) e que o shell sort O(n²) no pior caso e O(n*log n)
em média
"""
