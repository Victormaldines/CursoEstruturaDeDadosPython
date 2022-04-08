"""
1. Crie uma classe chamada aluno com os seguintes atributos:
    - Nome
    - Nota1
    - Nota2
    - Crie um construtor para a classe (__init__)

2. Crie as seguintes funções (métodos):
    - Calcula média, retornando a média aritmética entre as notas
    - Mostra dados, que somente imprime o valor de todos os atributos
    - Resultado, que verifica se o aluno está aprovado ou reprovado (se a
    média for maior ou igual a 6.0, o aluno está aprovado)

3. Crie dois objetos (aluno1 e aluno2) e teste as funções
"""

class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    
    def calculaMedia(self):
        return (self.nota1 + self.nota2) / 2

    def mostrarDados(self):
        print(self.nome)
        print(self.nota1)
        print(self.nota2)
    
    def resultado(self):
        if self.calculaMedia() >= 6.0:
            return 'Aluno aprovado'
        else:
            return 'Mano, aprovação moral'
    
aluno1 = Aluno('Gaules', 9, 7.5)
aluno2 = Aluno('Xande', 5.0, 6.0)

print(aluno1.calculaMedia())
aluno1.mostrarDados()
print(aluno1.resultado())

print(aluno2.calculaMedia())
aluno2.mostrarDados()
print(aluno2.resultado())
        