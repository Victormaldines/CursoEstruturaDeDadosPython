"""
VETORES NÃO ORDENADOS
Exemplo:
    * Controlar quais jogadores estão presentes no campo de treino (estrutura
    de dados)
    * Várias ações poderiam ser executadas
        * Inserir um jogador na estrutura de dados quando ele chegar ao campo
        * Verificar se um determinado jogador está presente, pesquisando o
        número do jogador na estrutura
        * Remover um jogador da estrutura de dados quando ele for pra casa

VETORES NÃO ORDENADOS - INSERÇÃO
    * Inserção de um novo jogador dentro do vetor
        _ _ _ _ _ _ _
        4 _ _ _ _ _ _
        4 2 _ _ _ _ _
        4 2 1 _ _ _ _
        4 2 1 8 _ _ _
        4 2 1 8 5 _ _

    * Único passo (insirido na primeira célula vaga do vetor)    
    * O algoritmo já conhece essa localização porque ela já sabe quantos itens
    já estão no vetor
    * O novo item é simplesmente inserido no próximo espaço disponível
    * Big-O constante - O(1)

VETORES NÃO ORDENADOS - PESQUISA
    * Percorrer cada posição do vetor
    
        4 2 1 8 5 _ _
        
        * Melhor caso: 4
        * Pior caso: 5 ou número que não existe
        * Em média, metado dos itens devem ser examinados (n/2) ~> n dividido por infinito ~> O(n)
        * Big-O linear - O(n)

VETORES NÃO ORDENADOS - EXCLUSÃO
    4 2 1 8 5 _ _                 
    4 2 _ 8 5 _ _   <- Teoria     4 2 1 8 5 _ _
    4 2 8 _ 5 _ _     Prática ->  4 2 8 8 5 _ _     (A última posição será 
    4 2 8 5 _ _ _                 4 2 8 5 5 _ _     sobrescrita na próxima inserção)
   
    * Pesquisar uma média de N/2 elementos (pesquisa linear)
        * Pior caso: N
    * Mover os elementos restantes (N/2 passos)
        * Pior caso: N
    * Big-O O(2n) = O(n)
    
VETORES NÃO ORDENADOS - DUPLICATAS
    * Deve-se decidir se itens com chaves duplicadas serão permitidos
    * Exemplo de um arquivo de funcionários
        * Se a chave for o número de registro
        * Se a chave for o sobrenome
    * Pesquisa: mesmo se encontrar o valor, o algoritmo terá que continuar procurando até a última célula (N passos)
    * Inserção: verificar cada item antes de fazer uma inserção (N passos)
    * Exclusão do primeiro item: N/2 comparação e N/2 movimentos
    * Exclusão de mais itens: verificar N células e mais de N/2 células
    
        4 2 1 8 5 2
        
"""
