"""
VETORES ORDENADOS
PESQUISA BINÁRIA
* Números de 1 até 100
* Pesquisar/adivinha o número 47

* números de 1 até 100
* 1 até 100 / 2 = 50
    * 50 é o número pesquisado? Não
    * 47 é menor ou maior do que 50? Menor
* 1 até 49 / 2 = 25
    * 25 é o número pesquisado? Não
    * 47 é menor ou maior do que 50? Maior
* 26 até 49 / 2 = 38
    * 38 é o número pesquisado? Não
    * 47 é menor ou maior do que 38? Maior
* 39 até 49 / 2 = 44
    * 44 é o número pesquisado? Não
    * 47 é maior ou menos do que 44? Maior
* 45 até 49 / 2 = 47
    * 47 é o número pesquisado? Sim

Outro Exemplo:
              *
    9   1 2 4 5 7 8 9    ~> 5 maior ou menor que 9? Menor (5 é o valor produrado? Não)
                  *
        _ _ _ _ 7 8 9    ~> 8 maior ou menor do que 9? Menor (8 é o valor procurado? Não)

        _ _ _ _ _ _ 9    ~> 9 é o valor procurado? Sim

"""