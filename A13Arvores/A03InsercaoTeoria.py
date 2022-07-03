'''
ÁRVORE BINÁRIA DE BUSCA - INSERÇÃO
    * Primeiro, o local para inserir deve ser encontrado
    * Segue-se o caminho da raiz até o devido nó folha, que será pai do novo nó
    * Quando esse pai for localizado, o novo nó será conectado como seu filho à esquerda ou à direita, dependendo da chave do novo nó ser menor, igual ou maior que a do pai
        * O filho à esquerda:
            Nó tem que ter uma chave menor que a de seu pai
        * O filho à direita:
            Nó tem que ter uma chave maior ou igual que a de seu pai
    * Visualização online: https://visualgo.net/en/bst
    * Big-O: O(log n) para o caso médio e O(n) no pior caso
'''